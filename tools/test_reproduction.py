#!/usr/bin/env python3
"""Unit tests of reporting infrastructure, not additional scientific evidence."""
from __future__ import annotations
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.reproduction import compare_results, numerical_environment, write_suite_evidence
from tools.reviewed_fields import review_field_differences


def raw(x): return json.dumps(x,allow_nan=False).encode()


class ReproductionTests(unittest.TestCase):
    def test_equal_and_serialization(self):
        r=raw({'x':1.})
        self.assertEqual(compare_results(r,r)['verdict'],'BYTE_IDENTICAL')
        self.assertEqual(compare_results(r,b'{"x":1.0}\n')['verdict'],'SERIALIZATION_ONLY')

    def test_metadata_not_physics(self):
        r=compare_results(raw({'environment':{'numpy':'x'},'value':1.}),raw({'environment':{'numpy':'y'},'value':1.}))
        self.assertEqual(r['verdict'],'METADATA_ONLY')
        self.assertTrue(r['scientific_values_identical'])

    def test_numeric_and_zero(self):
        r=compare_results(raw({'x':0.,'y':1.}),raw({'x':1e-14,'y':1.+1e-13}))
        self.assertEqual(r['verdict'],'WITHIN_NUMERICAL_TOLERANCE')
        self.assertEqual(r['differing_numeric_fields'],2)
        zero=r['differences'][0]
        self.assertIsNone(zero['reference_relative_difference'])
        self.assertEqual(zero['symmetric_relative_difference'],'1')

    def test_numeric_alert(self):
        r=compare_results(raw({'fidelity':.9}),raw({'fidelity':.901}))
        self.assertEqual(r['verdict'],'REVIEW_REQUIRED')
        self.assertEqual(r['regression_alerts'],1)

    def test_integer_and_bool_are_not_floats(self):
        for a,b in [(True,1),(10**12,10**12+1),(1,1.0)]:
            self.assertEqual(compare_results(raw({'x':a}),raw({'x':b}))['verdict'],'REVIEW_REQUIRED')

    def test_structural_and_status(self):
        for a,b in [({'x':[1,2]},{'x':[1]}),({'status':'PASS'},{'status':'FAIL'}),({'x':0},{}),({}, {'x':None})]:
            self.assertEqual(compare_results(raw(a),raw(b))['verdict'],'REVIEW_REQUIRED')

    def test_invalid(self):
        for r in [b'{"a":NaN}', b'{"a":Infinity}',b'{"a":1,"a":2}',b'bad', None]:
            self.assertEqual(compare_results(b'{}',r)['verdict'],'REVIEW_REQUIRED')
        self.assertEqual(compare_results(b'{"a":1e999}',b'{"a":1e999}')['verdict'],'REVIEW_REQUIRED')

    def test_nonfinite_metadata_is_invalid_before_metadata_filtering(self):
        reference=b'{"date":0,"environment":{},"value":1}'
        for observed in [b'{"date":1e999,"environment":{},"value":1}',
                         b'{"date":0,"environment":{"added":[-1e999]},"value":1}']:
            r=compare_results(reference,observed)
            self.assertEqual(r['verdict'],'REVIEW_REQUIRED')
            self.assertTrue(r['invalid_inputs'])
            self.assertFalse(review_field_differences(r,'dummy',reference,observed)['accepted'])
            json.dumps(r,allow_nan=False)

    def test_extreme_numbers(self):
        r=compare_results(raw({'x':1e-300}),raw({'x':1e100}))
        self.assertEqual(r['verdict'],'REVIEW_REQUIRED')
        self.assertIsInstance(r['differences'][0]['reference_relative_difference'],str)
        json.dumps(r,allow_nan=False)

    def test_pointer(self):
        r=compare_results(raw({'a/b':{'~':1.}}),raw({'a/b':{'~':1.1}}))
        self.assertEqual(r['differences'][0]['path'],'/a~1b/~0')

    def test_invalid_tolerance(self):
        for t in [-1.,float('nan'),float('inf')]:
            with self.assertRaises(ValueError):compare_results(b'{}',b'{}',atol=t)

    def test_evidence_is_not_rewritten(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'suite';r=b'{"x":0.0}';o=b'{"x":1e-14}'
            write_suite_evidence(p,b'print(1)',r,o,compare_results(r,o))
            self.assertEqual((p/'reference.json').read_bytes(),r)
            self.assertEqual((p/'observed.json').read_bytes(),o)
            with self.assertRaises(FileExistsError):write_suite_evidence(p,b'',r,o,{})

    def test_source_units_not_looser_general_tolerance(self):
        a={'groups':{'one_mode_number_superpositions':{'small_code':{'N':2000,'exact_scaled_losses':[6.0]}}}}
        b={'groups':{'one_mode_number_superpositions':{'small_code':{'N':2000,'exact_scaled_losses':[6.0+2e-8]}}}}
        r=compare_results(raw(a),raw(b));self.assertEqual(r['verdict'],'REVIEW_REQUIRED')
        v=review_field_differences(r,'01_pulse_matching',raw(a),raw(b));self.assertTrue(v['accepted'])
        self.assertEqual(r['verdict'],'REVIEW_REQUIRED') # The raw failed verdict is retained.
        b['groups']['one_mode_number_superpositions']['small_code']['exact_scaled_losses'][0]=10.0
        r=compare_results(raw(a),raw(b));self.assertFalse(review_field_differences(r,'01_pulse_matching',raw(a),raw(b))['accepted'])

    def test_solver_work_is_narrowly_scoped(self):
        a={'groups':{'finite_mean_and_fidelity':{'refined_largest_case':{'nfev':100}}},'cases':10}
        b={'groups':{'finite_mean_and_fidelity':{'refined_largest_case':{'nfev':112}}},'cases':10}
        r=compare_results(raw(a),raw(b));self.assertTrue(review_field_differences(r,'05_photon_collection',raw(a),raw(b))['accepted'])
        self.assertFalse(review_field_differences(r,'different_suite',raw(a),raw(b))['accepted'])
        b['cases']=11;r=compare_results(raw(a),raw(b))
        self.assertFalse(review_field_differences(r,'05_photon_collection',raw(a),raw(b))['accepted'])

    def test_changed_scaling_parameter_is_not_hidden(self):
        a={'groups':{'one_mode_number_superpositions':{'small_code':{'N':2000,'exact_scaled_losses':[6.0]}}}}
        b={'groups':{'one_mode_number_superpositions':{'small_code':{'N':3000,'exact_scaled_losses':[6.0+2e-8]}}}}
        r=compare_results(raw(a),raw(b));self.assertFalse(review_field_differences(r,'01_pulse_matching',raw(a),raw(b))['accepted'])

    def test_environment(self):
        r=numerical_environment()
        self.assertIn('numpy',r['packages'])
        self.assertNotIn('hostname',r)
        self.assertEqual(set(r['thread_settings']),{'OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'})
        json.dumps(r,allow_nan=False)

    def test_environment_uses_explicit_thread_settings(self):
        effective={'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'2'}
        with patch.dict('os.environ',{'OPENBLAS_NUM_THREADS':'17','OMP_NUM_THREADS':'23'}):
            self.assertEqual(numerical_environment(env=effective)['thread_settings'],effective)
            self.assertEqual(numerical_environment()['thread_settings']['OPENBLAS_NUM_THREADS'],'17')


if __name__=='__main__':unittest.main(verbosity=2)
