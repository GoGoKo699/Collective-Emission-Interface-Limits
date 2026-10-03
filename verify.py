#!/usr/bin/env python3
"""Verify preserved scripts/results and run standalone research suites.

No network requests are made and no reference result is overwritten.
Numerical reproduction is not independent proof or priority verification.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parent


def digest(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integrity():
    data=json.loads((ROOT/'provenance/SUITES.json').read_text())
    for suite in data['suites']:
        folder=ROOT/'tests'/suite['name']
        for filename,key in [('checks.py','checks_sha256'),('results.json','results_sha256')]:
            if digest(folder/filename)!=suite[key]:
                raise RuntimeError(f'Preserved file changed: {suite["name"]}/{filename}')
    links=0
    for path in ROOT.rglob('*.md'):
        text=path.read_text()
        if any(ord(c)<32 and c not in '\n\t\r' for c in text):
            raise RuntimeError(f'Control character: {path.relative_to(ROOT)}')
        if text.count('$$')%2 or text.count('```')%2:
            raise RuntimeError(f'Unbalanced display/code fences: {path.relative_to(ROOT)}')
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in target or target.startswith('#'):continue
            target=target.split('#',1)[0]
            if target and not (path.parent/target).exists():
                raise RuntimeError(f'Broken local link: {path.relative_to(ROOT)} -> {target}')
            links+=1
    return data,links


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--integrity-only',action='store_true')
    parser.add_argument('--suite',help='Run one suite, by its exact directory name')
    parser.add_argument('--timeout',type=float,default=240.,help='Seconds permitted for each suite')
    parser.add_argument('--output',type=Path,default=Path.cwd()/'verification-report.json')
    args=parser.parse_args()
    if args.timeout<=0:parser.error('--timeout must be positive')
    manifest,links=integrity()
    suites=manifest['suites']
    if args.suite:
        suites=[s for s in suites if s['name']==args.suite]
        if not suites:parser.error('Unknown suite name')
    print(f'PASS integrity: {len(manifest["suites"])} suite identities; {links} local links',flush=True)
    if args.integrity_only:return
    destination=args.output.resolve()
    if destination.is_relative_to((ROOT/'tests').resolve()):
        parser.error('Output cannot overwrite test code or reference data')
    env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1'}
    rows=[]
    with tempfile.TemporaryDirectory(prefix='collective-interface-verify-') as tempdir:
        temp=Path(tempdir)
        for suite in suites:
            folder=ROOT/'tests'/suite['name'];output=temp/(suite['name']+'.json')
            start=time.monotonic()
            try:
                run=subprocess.run([sys.executable,str(folder/'checks.py'),'--output',str(output)],
                                   cwd=folder,env=env,text=True,capture_output=True,timeout=args.timeout)
                returncode,stdout,stderr=run.returncode,run.stdout,run.stderr
            except subprocess.TimeoutExpired as error:
                returncode=124
                stdout=error.stdout or '';stderr=error.stderr or ''
                if isinstance(stdout,bytes):stdout=stdout.decode(errors='replace')
                if isinstance(stderr,bytes):stderr=stderr.decode(errors='replace')
                stderr+=f'\nPer-suite timeout of {args.timeout} seconds exceeded.'
            observed=output.read_bytes() if output.exists() else None
            saved=(folder/'results.json').read_bytes()
            parsed=json.loads(observed) if observed else {}
            clean=lambda s:s.replace(str(temp),'[TEMP]').replace(str(ROOT),'[REPOSITORY]')
            row=dict(name=suite['name'],returncode=returncode,status=parsed.get('status','NO RESULT'),
                     groups=parsed.get('group_count'),cases=parsed.get('cases',parsed.get('parameter_cases')),
                     result_byte_identical=observed==saved,result_JSON_identical=parsed==json.loads(saved),
                     elapsed_seconds=round(time.monotonic()-start,3),stdout=clean(stdout),stderr=clean(stderr))
            rows.append(row)
            print(f'{row["name"]}: {row["status"]}; saved results identical: {row["result_byte_identical"]}',flush=True)
            if returncode:break
    integrity()
    passed=len(rows)==len(suites) and all(r['returncode']==0 and r['status']=='PASS' for r in rows)
    report=dict(status='PASS' if passed else 'FAIL',date='2026-10-03',python=platform.python_version(),
                suite_count=len(rows),group_count=sum(r['groups'] or 0 for r in rows),
                case_count=sum(r['cases'] or 0 for r in rows),
                all_reference_results_byte_identical=all(r['result_byte_identical'] for r in rows),
                originals_unchanged=True,runs=rows,
                scope='Author-side reproducibility and source preservation, not independent mathematical or priority review.')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print('WROTE',destination,flush=True)
    if not passed:raise SystemExit(1)
    if not report['all_reference_results_byte_identical']:
        print('Note: calculations passed but exact reference bytes differ. Check environment and report numerical differences explicitly.')

if __name__=='__main__':main()
