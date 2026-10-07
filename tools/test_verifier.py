#!/usr/bin/env python3
"""Focused verifier provenance/safety fixtures, not executions of scientific suites."""
from __future__ import annotations
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import verify


class VerifierTests(unittest.TestCase):
    def setUp(self):
        self.temporary=tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root=Path(self.temporary.name)/'repo'
        self.suite=self.root/'tests'/'fixture'
        self.suite.mkdir(parents=True)
        self.reference=b'{"status":"PASS","group_count":1,"cases":1,"date":0}\n'
        (self.suite/'checks.py').write_text('# Synthetic reporting fixture only.\n')
        (self.suite/'results.json').write_bytes(self.reference)
        (self.root/'verify.py').write_text('# Source file that must remain untouched.\n')
        self.artifacts=self.root/'verification-artifacts'
        self.output=self.root/'verification-report.json'
        self.manifest={'suites':[{'name':'fixture',
                                'checks_sha256':verify.digest(self.suite/'checks.py'),
                                'results_sha256':verify.digest(self.suite/'results.json')}]}
        (self.root/'provenance').mkdir()
        (self.root/'provenance/SUITES.json').write_text(json.dumps(self.manifest)+'\n')
        self.started=datetime(2031,4,2,23,59,59,tzinfo=timezone.utc)
        self.finished=datetime(2031,4,3,0,0,1,tzinfo=timezone.utc)

    def run_fixture(self,observed=None,output=None):
        generated=self.reference if observed is None else observed
        output=self.output if output is None else output
        def run(command,**kwargs):
            Path(command[-1]).write_bytes(generated)
            return subprocess.CompletedProcess(command,0,'PASS fixture\n','')
        def environment(*,env):
            return {'thread_settings':{key:env.get(key) for key in
                                      ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')}}
        args=['verify.py','--output',str(output),'--artifacts-dir',str(self.artifacts),'--require-reference']
        with patch.object(verify,'ROOT',self.root), \
             patch.object(verify,'integrity',return_value=(self.manifest,0)), \
             patch.object(verify,'datetime') as clock, \
             patch.object(verify,'numerical_environment',side_effect=environment), \
             patch.object(verify.subprocess,'run',side_effect=run) as suite_run, \
             patch.object(sys,'argv',args), \
             patch.dict(os.environ,{'OPENBLAS_NUM_THREADS':'17','OMP_NUM_THREADS':'23'}), \
             redirect_stdout(io.StringIO()),redirect_stderr(io.StringIO()):
            clock.now.side_effect=[self.started,self.finished]
            try:
                verify.main()
                exit_code=0
            except SystemExit as error:
                exit_code=error.code
            return exit_code,suite_run

    def test_run_records_actual_utc_times_and_effective_threads(self):
        code,suite_run=self.run_fixture()
        self.assertEqual(code,0)
        report=json.loads(self.output.read_text())
        self.assertEqual(report['date'],'2031-04-02')
        self.assertEqual(report['started_at'],self.started.isoformat())
        self.assertEqual(report['finished_at'],self.finished.isoformat())
        recorded=json.loads((self.artifacts/'environment.json').read_text())['thread_settings']
        effective=suite_run.call_args.kwargs['env']
        self.assertEqual(recorded,{key:effective.get(key) for key in recorded})
        self.assertEqual(recorded['OPENBLAS_NUM_THREADS'],'1')
        self.assertEqual(recorded['OMP_NUM_THREADS'],'1')

    def test_rejects_source_output_before_execution(self):
        source=self.root/'verify.py'
        original=source.read_bytes()
        code,suite_run=self.run_fixture(output=source)
        self.assertEqual(code,2)
        suite_run.assert_not_called()
        self.assertEqual(source.read_bytes(),original)
        self.assertFalse(self.artifacts.exists())

    def test_protects_maintained_directories_and_raw_artifacts(self):
        with patch.object(verify,'ROOT',self.root):
            for relative in ['provenance/SUITES.json','tests/fixture/results.json',
                             'docs/new-report.json','work_orders/new-report.json','.git/config',
                             'verification-artifacts/fixture/observed.json',
                             'verification-artifacts/environment.json']:
                with self.subTest(path=relative),self.assertRaises(ValueError):
                    verify.validate_output_destination(self.root/relative,self.artifacts)

    def test_allows_generated_summaries_and_fresh_custom_outputs(self):
        for name in ['verification-report.json','rerun.json']:
            (self.root/name).write_text('{}\n')
        with patch.object(verify,'ROOT',self.root):
            for path in [self.output,self.root/'rerun.json',self.root/'new-summary.json',
                         self.artifacts/'verification-report.json',self.root.parent/'external-summary.json']:
                verify.validate_output_destination(path,self.artifacts)

    def test_invalid_metadata_fails_gate_and_preserves_raw_output(self):
        observed=b'{"status":"PASS","group_count":1,"cases":1,"date":1e999}\n'
        code,_=self.run_fixture(observed=observed)
        self.assertEqual(code,1)
        report=json.loads(self.output.read_text())
        self.assertEqual(report['status'],'FAIL')
        self.assertFalse(report['reference_comparison_passed'])
        self.assertEqual(report['finished_at'],self.finished.isoformat())
        self.assertEqual((self.artifacts/'fixture'/'observed.json').read_bytes(),observed)

    def test_integrity_accepts_contact_links_and_reads_llms_guide(self):
        (self.root/'README.md').write_text(
            '[Contact](mailto:reader@example.org) [Guide](llms.txt)\n')
        (self.root/'llms.txt').write_text(
            '[Contact](MAILTO:reader@example.org) [Readme](README.md)\n'
            '[Source](https://example.org/source)\n')
        with patch.object(verify,'ROOT',self.root):
            manifest,links=verify.integrity()
        self.assertEqual(manifest,self.manifest)
        self.assertEqual(links,2)

    def test_integrity_rejects_broken_local_markdown_link(self):
        (self.root/'README.md').write_text(
            '[Contact](mailto:reader@example.org) [Missing](missing.md)\n')
        with patch.object(verify,'ROOT',self.root), \
             self.assertRaisesRegex(RuntimeError,'Broken local link: README.md -> missing.md'):
            verify.integrity()

    def test_integrity_rejects_broken_local_llms_link(self):
        (self.root/'README.md').write_text('# Fixture\n')
        (self.root/'llms.txt').write_text(
            '[Source](https://example.org/source) [Missing](docs/missing.md#claim)\n')
        with patch.object(verify,'ROOT',self.root), \
             self.assertRaisesRegex(RuntimeError,'Broken local link: llms.txt -> docs/missing.md'):
            verify.integrity()


if __name__=='__main__':unittest.main(verbosity=2)
