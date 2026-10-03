"""Two source-inspected reporting rules; raw comparisons are never rewritten.

01 reports N**2*(1-fidelity) as a perturbative diagnostic. Compare its original
infidelity units as well as retaining the raw scaled difference. 05 records
solve_ivp.nfev, a work counter, not a physical quantity or test-case count.
No other field receives these exceptions. General tolerances are unchanged.
"""
from __future__ import annotations
from decimal import Decimal, localcontext
import re
from typing import Any
from .reproduction import load_json

POLICY_ID='source-reviewed-fields-v1'


def _at(data: Any, parts: list[str]) -> Any:
    for part in parts:
        data=data[int(part)] if isinstance(data,list) else data[part]
    return data


def review_field_differences(raw: dict[str, Any], suite: str,
                             reference: bytes, observed: bytes | None) -> dict[str, Any]:
    reviewed=[];unresolved=[]
    if raw['invalid_inputs']:
        return dict(policy=POLICY_ID,accepted=False,raw_alerts=raw['regression_alerts'],
                    unresolved_paths=['<invalid input>'],reviewed_fields=[])
    a=load_json(reference);b=load_json(observed)
    for d in raw['differences']:
        if d['category']=='metadata':
            continue
        path=d['path'];kind=d['kind']
        # A name match alone is insufficient: only these current suite-05 paths.
        work=suite=='05_photon_collection' and re.fullmatch(
            r'/groups/finite_mean_and_fidelity/(finite_rows/\d+/mean|refined_largest_case)/nfev',path)
        if work and kind=='number' and all(type(d[k]) is int and d[k]>=0 for k in ['reference','observed']):
            reviewed.append(dict(path=path,role='solver_work',reference=d['reference'],observed=d['observed'],
                                 justification='tests/05_photon_collection/checks.py:90 stores sol.nfev; not a physical result.'))
            continue
        scale_parent=None
        if suite=='01_pulse_matching' and kind=='number':
            if re.fullmatch(r'/groups/orthogonal_error_components/fixed_m_checks/\d+/scaled_loss',path):
                scale_parent=path.split('/')[1:-1]
            elif re.fullmatch(r'/groups/one_mode_number_superpositions/small_code/exact_scaled_losses/\d+',path):
                scale_parent=['groups','one_mode_number_superpositions','small_code']
        if scale_parent is not None:
            try:
                na=_at(a,scale_parent)['N'];nb=_at(b,scale_parent)['N']
            except (KeyError,TypeError,IndexError):
                na=nb=None
            if type(na) is int and na>0 and na==nb:
                with localcontext() as ctx:
                    ctx.prec=80
                    scale=Decimal(na)**2
                    va=Decimal(str(d['reference']))/scale;vb=Decimal(str(d['observed']))/scale
                    delta=abs(va-vb)
                    bound=Decimal(str(raw['absolute_tolerance']))+Decimal(str(raw['relative_tolerance']))*max(abs(va),abs(vb))
                    accepted=delta<=bound
                reviewed.append(dict(path=path,role='N_squared_infidelity',N=na,
                                     original_unit_absolute_difference=str(delta),
                                     original_unit_alert_threshold=str(bound),accepted=accepted,
                                     justification='tests/01_pulse_matching/checks.py:142-148 and 184-189 explicitly store N**2*(1-fidelity).'))
                if not accepted:unresolved.append(path)
                continue
        if kind!='number' or d.get('integer_change',False) or not d.get('within_tolerance',False):
            unresolved.append(path)
    return dict(policy=POLICY_ID,accepted=not unresolved,raw_alerts=raw['regression_alerts'],
                unresolved_paths=unresolved,reviewed_fields=reviewed,
                scope='Only declared source-derived units/work counters are interpreted; every raw difference and raw verdict remains unchanged.')
