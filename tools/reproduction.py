"""Field-level JSON evidence for numerical reproduction, not scientific proofs.

Only a top-level ``environment`` object and ``date`` are metadata. Everything
else, including seeds, integer counters, strings and structure, is compared.
Tolerances are regression alerts, not accuracy certificates for calculations.
"""
from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
from decimal import Decimal, localcontext
import hashlib
import importlib.metadata
import io
import json
import math
import os
from pathlib import Path
import platform
from typing import Any

DEFAULT_ATOL = 1e-10
DEFAULT_RTOL = 1e-9


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _reject_constant(value: str) -> None:
    raise ValueError(f'Nonfinite JSON constant: {value}')


def _unique_object(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise ValueError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def load_json(data: bytes) -> Any:
    return json.loads(data, parse_constant=_reject_constant, object_pairs_hook=_unique_object)


def _pointer(parts: tuple[str, ...]) -> str:
    return ''.join('/' + p.replace('~', '~0').replace('/', '~1') for p in parts)


def _number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def compare_results(reference: bytes, observed: bytes | None,
                    atol: float = DEFAULT_ATOL, rtol: float = DEFAULT_RTOL) -> dict[str, Any]:
    if not all(math.isfinite(x) and x >= 0 for x in (atol, rtol)):
        raise ValueError('Tolerances must be finite and nonnegative.')
    result: dict[str, Any] = {
        'reference_sha256': digest(reference),
        'observed_sha256': digest(observed) if observed is not None else None,
        'byte_identical': observed == reference,
        'absolute_tolerance': atol, 'relative_tolerance': rtol,
        'tolerance_rule': 'abs(a-b) <= atol + rtol*max(abs(a),abs(b))',
        'metadata_paths': ['/environment', '/date'],
        'scope': 'Field comparison and regression alert; not a numerical error proof or independent review.'
    }
    differences: list[dict[str, Any]] = []
    invalid: list[dict[str, str]] = []
    try:
        expected = load_json(reference)
    except (ValueError, UnicodeError) as exc:
        expected = None
        invalid.append({'side': 'reference', 'error': str(exc)})
    try:
        actual = load_json(observed) if observed is not None else None
        if observed is None:
            invalid.append({'side': 'observed', 'error': 'No output was produced.'})
    except (ValueError, UnicodeError) as exc:
        actual = None
        invalid.append({'side': 'observed', 'error': str(exc)})

    compared = 0

    def walk(a: Any, b: Any, parts: tuple[str, ...] = ()) -> None:
        nonlocal compared
        metadata = bool(parts and parts[0] in ('environment', 'date'))
        entry = {'path': _pointer(parts), 'category': 'metadata' if metadata else 'scientific'}
        if isinstance(a, dict) and isinstance(b, dict):
            for key in sorted(a.keys() | b.keys()):
                if key not in a or key not in b:
                    differences.append({**entry, 'path': _pointer(parts+(key,)),
                                        'kind': 'added' if key not in a else 'removed',
                                        'reference': a.get(key), 'observed': b.get(key),
                                        'category': 'metadata' if (parts+(key,))[0] in ('environment','date') else 'scientific'})
                else:
                    walk(a[key], b[key], parts+(key,))
            return
        if isinstance(a, list) and isinstance(b, list):
            if len(a) != len(b):
                differences.append({**entry, 'kind': 'list_length', 'reference': len(a), 'observed': len(b)})
            for i in range(min(len(a),len(b))):
                walk(a[i], b[i], parts+(str(i),))
            return
        if _number(a) and _number(b):
            compared += 1
            if (isinstance(a,float) and not math.isfinite(a)) or (isinstance(b,float) and not math.isfinite(b)):
                differences.append({**entry, 'kind': 'nonfinite_number', 'reference': str(a), 'observed': str(b)})
                return
            if a == b and type(a) is type(b):
                return
            with localcontext() as ctx:
                ctx.prec = 80
                da, db = Decimal(str(a)), Decimal(str(b))
                absolute = abs(da-db)
                scale = max(abs(da),abs(db))
                relative = absolute/scale if scale else Decimal(0)
                ref_relative = absolute/abs(da) if da else None
                within = absolute <= Decimal(str(atol)) + Decimal(str(rtol))*scale
            # Keep exact decimal diagnostics in strings, avoiding overflow for tiny baselines.
            differences.append({**entry, 'kind': 'number' if type(a) is type(b) else 'numeric_type',
                                'reference': a, 'observed': b, 'absolute_difference': str(absolute),
                                'symmetric_relative_difference': str(relative),
                                'reference_relative_difference': str(ref_relative) if ref_relative is not None else None,
                                'reference_is_zero': a == 0, 'within_tolerance': bool(within),
                                'integer_change': isinstance(a,int) and isinstance(b,int) and a != b})
            return
        if type(a) is not type(b):
            differences.append({**entry, 'kind': 'type', 'reference': a, 'observed': b})
        elif a != b:
            differences.append({**entry, 'kind': 'value', 'reference': a, 'observed': b})

    if not invalid:
        walk(expected, actual)
    numeric = [d for d in differences if d['category']=='scientific' and 'absolute_difference' in d]
    metadata = [d for d in differences if d['category']=='metadata']
    other = [d for d in differences if d['category']=='scientific' and 'absolute_difference' not in d]
    alerts = [d for d in differences if d['category']=='scientific' and
              (d.get('kind') != 'number' or d.get('integer_change',False) or not d.get('within_tolerance',False))]
    def maximum(key: str) -> dict[str, Any] | None:
        if not numeric:
            return None
        d = max(numeric, key=lambda row: Decimal(row[key]))
        return {k:d[k] for k in ('path','reference','observed',key)}
    if invalid or alerts:
        verdict = 'REVIEW_REQUIRED'
    elif result['byte_identical']:
        verdict = 'BYTE_IDENTICAL'
    elif not differences:
        verdict = 'SERIALIZATION_ONLY'
    elif not numeric and not other:
        verdict = 'METADATA_ONLY'
    else:
        verdict = 'WITHIN_NUMERICAL_TOLERANCE'
    result.update(verdict=verdict, json_identical=not invalid and not differences,
                  scientific_values_identical=not invalid and not numeric and not other,
                  numeric_fields_compared=compared, differing_numeric_fields=len(numeric),
                  differing_metadata_fields=len(metadata), differing_nonnumeric_scientific_fields=len(other),
                  regression_alerts=len(alerts), max_absolute=maximum('absolute_difference'),
                  max_symmetric_relative=maximum('symmetric_relative_difference'),
                  difference_kinds=dict(Counter(d['kind'] for d in differences)),
                  invalid_inputs=invalid, differences=differences)
    return result


def numerical_environment() -> dict[str, Any]:
    """Allowlisted runtime details; never dump credentials or the full environment."""
    result: dict[str, Any] = {
        'python': platform.python_version(), 'python_implementation': platform.python_implementation(),
        'platform_system': platform.system(), 'platform_release': platform.release(),
        'machine': platform.machine(), 'processor': platform.processor(),
        'thread_settings': {key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        'packages': {},
    }
    for name in ('numpy','scipy','mpmath'):
        try:
            result['packages'][name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            result['packages'][name] = None
    cpu_info = Path('/proc/cpuinfo')
    if cpu_info.is_file():
        for line in cpu_info.read_text(errors='replace').splitlines():
            if line.startswith('model name'):
                result['cpu_model'] = line.partition(':')[2].strip()
                break
    for name in ('numpy','scipy'):
        try:
            module = __import__(name)
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                module.show_config()
            result[name+'_configuration'] = buffer.getvalue()
        except Exception as exc:
            result[name+'_configuration_error'] = f'{type(exc).__name__}: {exc}'
    return result


def write_suite_evidence(folder: Path, script: bytes, reference: bytes,
                         observed: bytes | None, comparison: dict[str, Any]) -> None:
    folder.mkdir(parents=True, exist_ok=False)
    (folder/'checks.py').write_bytes(script)
    (folder/'reference.json').write_bytes(reference)
    if observed is not None:
        (folder/'observed.json').write_bytes(observed)
    (folder/'comparison.json').write_text(json.dumps(comparison,indent=2,allow_nan=False)+'\n')
