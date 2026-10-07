#!/usr/bin/env python3
"""Verify preserved scripts/results and run standalone research suites.

No network requests are made and no reference result is overwritten.
Numerical reproduction is not independent proof or priority verification.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
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
from tools.reproduction import compare_results, numerical_environment, write_suite_evidence, DEFAULT_ATOL, DEFAULT_RTOL
from tools.reviewed_fields import review_field_differences

ROOT=Path(__file__).resolve().parent
MAINTAINED_DIRECTORIES=('tests','provenance','research','literature','tools','.github','docs','work_orders','.git')


def digest(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_output_destination(destination:Path, artifacts:Path|None=None)->None:
    """Keep a summary from replacing source files or the raw evidence it summarizes."""
    if destination == ROOT or ROOT.is_relative_to(destination):
        raise ValueError('Output cannot overwrite the repository or an ancestor')
    if any(destination.is_relative_to((ROOT/p).resolve()) for p in MAINTAINED_DIRECTORIES):
        raise ValueError('Output cannot overwrite maintained source or evidence directories')
    generated_reports={ROOT/'verification-report.json',ROOT/'rerun.json'}
    if destination.is_relative_to(ROOT) and destination.exists() and destination not in generated_reports:
        raise ValueError('Output cannot replace an existing repository file; choose a new report path')
    if artifacts and destination.is_relative_to(artifacts) and destination != artifacts/'verification-report.json':
        raise ValueError('Output inside artifacts must be verification-report.json, preserving raw suite evidence')


def integrity():
    data=json.loads((ROOT/'provenance/SUITES.json').read_text())
    for suite in data['suites']:
        folder=ROOT/'tests'/suite['name']
        for filename,key in [('checks.py','checks_sha256'),('results.json','results_sha256')]:
            if digest(folder/filename)!=suite[key]:
                raise RuntimeError(f'Preserved file changed: {suite["name"]}/{filename}')
    links=0
    reading_files=list(ROOT.rglob('*.md'))
    llms_guide=ROOT/'llms.txt'
    if llms_guide.is_file():reading_files.append(llms_guide)
    for path in reading_files:
        text=path.read_text()
        if any(ord(c)<32 and c not in '\n\t\r' for c in text):
            raise RuntimeError(f'Control character: {path.relative_to(ROOT)}')
        if text.count('$$')%2 or text.count('```')%2:
            raise RuntimeError(f'Unbalanced display/code fences: {path.relative_to(ROOT)}')
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in target or target.startswith('#') or target.lower().startswith('mailto:'):continue
            target=target.split('#',1)[0]
            if target and not (path.parent/target).exists():
                raise RuntimeError(f'Broken local link: {path.relative_to(ROOT)} -> {target}')
            links+=1
    return data,links


def main():
    started_at=datetime.now(timezone.utc)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--integrity-only',action='store_true')
    parser.add_argument('--suite',help='Run one suite, by its exact directory name')
    parser.add_argument('--timeout',type=float,default=240.,help='Seconds permitted for each suite')
    parser.add_argument('--output',type=Path,default=Path.cwd()/'verification-report.json')
    parser.add_argument('--artifacts-dir',type=Path,help='New directory for raw outputs, comparisons and allowlisted environment')
    parser.add_argument('--require-reference',action='store_true',help='Fail on structural or out-of-tolerance scientific differences')
    parser.add_argument('--atol',type=float,default=DEFAULT_ATOL,help='Absolute regression-alert tolerance, not an accuracy certificate')
    parser.add_argument('--rtol',type=float,default=DEFAULT_RTOL,help='Symmetric relative regression-alert tolerance')
    args=parser.parse_args()
    compare_results(b'{}',b'{}',args.atol,args.rtol) # Validate tolerances before running suites.
    if args.timeout<=0:parser.error('--timeout must be positive')
    manifest,links=integrity()
    suites=manifest['suites']
    if args.suite:
        suites=[s for s in suites if s['name']==args.suite]
        if not suites:parser.error('Unknown suite name')
    print(f'PASS integrity: {len(manifest["suites"])} suite identities; {links} local links',flush=True)
    if args.integrity_only:return
    destination=args.output.resolve()
    env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1'}
    artifacts=args.artifacts_dir.resolve() if args.artifacts_dir else None
    try:validate_output_destination(destination,artifacts)
    except ValueError as error:parser.error(str(error))
    if artifacts:
        if artifacts == ROOT or ROOT.is_relative_to(artifacts):
            parser.error('Artifacts must not overwrite the repository or an ancestor')
        if any(artifacts.is_relative_to((ROOT/p).resolve()) for p in MAINTAINED_DIRECTORIES):
            parser.error('Artifacts cannot be written into maintained source or evidence directories')
        artifacts.mkdir(parents=True,exist_ok=False)
        environment=numerical_environment(env=env)
        environment['revision']={key:os.environ.get(key) for key in ['GITHUB_SHA','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT']}
        (artifacts/'environment.json').write_text(json.dumps(environment,indent=2,allow_nan=False)+'\n')
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
            comparison=compare_results(saved,observed,args.atol,args.rtol)
            review=review_field_differences(comparison,suite['name'],saved,observed)
            try:parsed=json.loads(observed) if observed else {}
            except (ValueError,UnicodeError):parsed={}
            if not isinstance(parsed,dict):parsed={}
            if artifacts:
                write_suite_evidence(artifacts/suite['name'],(folder/'checks.py').read_bytes(),saved,observed,comparison)
                (artifacts/suite['name']/'reviewed-comparison.json').write_text(json.dumps(review,indent=2,allow_nan=False)+'\n')
            clean=lambda s:s.replace(str(temp),'[TEMP]').replace(str(ROOT),'[REPOSITORY]')
            row=dict(name=suite['name'],returncode=returncode,status=parsed.get('status','NO RESULT'),
                     groups=parsed.get('group_count'),cases=parsed.get('cases',parsed.get('parameter_cases')),
                     result_byte_identical=observed==saved,result_JSON_identical=parsed==json.loads(saved),
                     elapsed_seconds=round(time.monotonic()-start,3),stdout=clean(stdout),stderr=clean(stderr),
                     comparison={k:v for k,v in comparison.items() if k!='differences'},review=review)
            rows.append(row)
            print(f'{row["name"]}: {row["status"]}; saved results identical: {row["result_byte_identical"]}',flush=True)
            print(f'  reference comparison: {comparison["verdict"]}; scientific numeric differences: {comparison["differing_numeric_fields"]}',flush=True)
            print(f'  source-reviewed comparison accepted: {review["accepted"]}; unresolved paths: {len(review["unresolved_paths"])}',flush=True)
            if returncode:break
    integrity()
    passed=len(rows)==len(suites) and all(r['returncode']==0 and r['status']=='PASS' for r in rows)
    reference_ok=all(r['review']['accepted'] for r in rows)
    assertions_passed=passed
    if args.require_reference:passed=passed and reference_ok
    finished_at=datetime.now(timezone.utc)
    report=dict(scientific_assertions_passed=assertions_passed,reference_comparison_passed=reference_ok,
                reference_comparison_required=args.require_reference,status='PASS' if passed else 'FAIL',
                date=started_at.date().isoformat(),started_at=started_at.isoformat(),finished_at=finished_at.isoformat(),
                python=platform.python_version(),
                suite_count=len(rows),group_count=sum(r['groups'] or 0 for r in rows),
                case_count=sum(r['cases'] or 0 for r in rows),
                all_reference_results_byte_identical=all(r['result_byte_identical'] for r in rows),
                originals_unchanged=True,runs=rows,
                scope='Author-side reproducibility and source preservation, not independent mathematical or priority review.')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    if artifacts:(artifacts/'verification-report.json').write_bytes(destination.read_bytes())
    print('WROTE',destination,flush=True)
    if not passed:raise SystemExit(1)
    if not report['all_reference_results_byte_identical']:
        print('Exact reference bytes differ; field-level verdicts are reported separately. Raw evidence is retained when --artifacts-dir is provided.')

if __name__=='__main__':main()
