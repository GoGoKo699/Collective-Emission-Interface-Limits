#!/usr/bin/env python3
"""Capture outputs of the unmodified pre-diagnostic runner for issue #7.

The only intervention copies temporary files immediately before their normal
cleanup. The original runner and scientific scripts execute without rewriting.
"""
from __future__ import annotations
import argparse
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import runpy
import shutil
import sys
import tempfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.reproduction import compare_results, numerical_environment


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--runner',type=Path,required=True)
    ap.add_argument('--capture-dir',type=Path,required=True)
    args=ap.parse_args()
    runner=args.runner.resolve();out=args.capture_dir.resolve();root=runner.parent
    content=runner.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
    if blob!='be56c4cd9971405b75e2363a49c88a27378c20ef':
        raise ValueError('Not the recorded pre-diagnostic runner.')
    if out==root or root.is_relative_to(out) or any(out.is_relative_to((root/p).resolve()) for p in ['tests','provenance','research','literature','tools','.github']):
        raise ValueError('Capture directory must not overwrite maintained files.')
    out.mkdir(parents=True,exist_ok=False)
    original=tempfile.TemporaryDirectory
    @contextmanager
    def capture(*a,**kw):
        with original(*a,**kw) as folder:
            try:
                yield folder
            finally:
                if kw.get('prefix')=='collective-interface-verify-':
                    shutil.copytree(folder,out/'generated')
    tempfile.TemporaryDirectory=capture
    old_argv=sys.argv
    sys.argv=[str(runner),'--output',str(out/'original-report.json')]
    try:
        runpy.run_path(str(runner),run_name='__main__')
    finally:
        tempfile.TemporaryDirectory=original
        sys.argv=old_argv
    manifest=json.loads((root/'provenance/SUITES.json').read_text())
    rows=[]
    for suite in manifest['suites']:
        expected=(root/'tests'/suite['name']/'results.json').read_bytes()
        observed=(out/'generated'/(suite['name']+'.json')).read_bytes()
        comparison=compare_results(expected,observed)
        rows.append({'name':suite['name'],**comparison})
    record={'original_runner_blob':blob,'runtime':numerical_environment(),
            'all_byte_identical':all(r['byte_identical'] for r in rows),
            'comparisons':rows,'scope':'Reexecution of original runner with output retention only; not recovery of the discarded historical outputs.'}
    (out/'comparison.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print('Original runner, all exact:',record['all_byte_identical'],flush=True)


if __name__=='__main__':main()
