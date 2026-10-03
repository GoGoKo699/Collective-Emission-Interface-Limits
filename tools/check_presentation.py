#!/usr/bin/env python3
"""Check Markdown math boundaries and tables without changing research content.

Accepts GitHub's $...$, $`...`$, $$...$$ and fenced math. This is a structural
check, not a TeX renderer, visual check, scientific test or proof verification.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def escaped(text: str, pos: int) -> bool:
    n = 0
    while pos > 0 and text[pos - 1] == '\\':
        pos -= 1
        n += 1
    return bool(n % 2)


def inspect(text: str, name: str = '<text>') -> dict:
    errors: list[str] = []
    expressions: list[dict] = []
    fence: str | None = None
    fence_math = False
    display = False
    pending: list[str] = []
    start = 0
    columns: int | None = None

    def error(line: int, message: str) -> None:
        errors.append(f'{name}:{line}: {message}')

    def math(tex: str, line: int, block: bool, table: bool = False) -> None:
        if not tex.strip():
            error(line, 'Empty mathematics')
        # Escaped braces are glyphs, not grouping braces.
        depth = 0
        for i, c in enumerate(tex):
            if escaped(tex, i):
                continue
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth < 0:
                    error(line, 'Unbalanced TeX grouping braces')
                    break
        if depth:
            error(line, 'Unbalanced TeX grouping braces')
        if table and '|' in tex:
            error(line, r'Literal pipe inside table mathematics; use \vert or \Vert')
        if '`' in tex or '$' in tex:
            error(line, 'Nested Markdown delimiter inside mathematics')
        expressions.append(dict(line=line, display=block, tex=tex))

    for number, line in enumerate(text.splitlines(), 1):
        if any(ord(c) < 32 and c != '\t' for c in line):
            error(number, 'Unexpected control character')
        mark = re.match(r'^\s*(`{3,}|~{3,})([^\n]*)$', line)
        if fence:
            if mark and mark[1][0] == fence[0] and len(mark[1]) >= len(fence) and not mark[2].strip():
                if fence_math:
                    math('\n'.join(pending), start, True)
                fence = None
                pending = []
            elif fence_math:
                pending.append(line)
            continue
        if mark:
            if display:
                error(number, 'Code fence inside unclosed display mathematics')
            fence, fence_math, start = mark[1], mark[2].strip() == 'math', number
            pending = []
            columns = None
            continue
        table = line.lstrip().startswith('|') and not display
        if table:
            count = sum(c == '|' and not escaped(line, i) for i, c in enumerate(line))
            if columns is not None and count != columns:
                error(number, 'Inconsistent table columns')
            columns = count
        else:
            columns = None
        i = 0
        while i < len(line):
            if display:
                j = i
                while True:
                    j = line.find('$$', j)
                    if j < 0 or not escaped(line, j):
                        break
                    j += 2
                if j < 0:
                    pending.append(line[i:])
                    break
                pending.append(line[i:j])
                math('\n'.join(pending), start, True)
                display, pending, i = False, [], j + 2
                continue
            if line[i] == '`':
                match = re.match(r'`+', line[i:])
                delim = match[0]
                j = line.find(delim, i + len(delim))
                if j < 0:
                    error(number, 'Unclosed inline-code delimiter')
                    break
                i = j + len(delim)
                continue
            if line[i] != '$' or escaped(line, i):
                i += 1
                continue
            if line.startswith('$$', i):
                display, start, pending, i = True, number, [], i + 2
                continue
            if line.startswith('$`', i):
                j = line.find('`$', i + 2)
                if j < 0:
                    error(number, 'Unclosed GitHub inline-math delimiter')
                    break
                math(line[i + 2:j], number, False, table)
                if line[j + 2:j + 3] == '`':
                    error(number, 'Stray code delimiter after inline mathematics')
                i = j + 2
            else:
                j = i + 1
                while True:
                    j = line.find('$', j)
                    if j < 0 or not escaped(line, j):
                        break
                    j += 1
                if j < 0:
                    error(number, 'Unclosed inline-math delimiter')
                    break
                math(line[i + 1:j], number, False, table)
                i = j + 1
    if fence:
        error(start, 'Unclosed fenced block')
    if display:
        error(start, 'Unclosed display mathematics')
    return dict(path=name, errors=errors, expressions=expressions)


class PresentationTests(unittest.TestCase):
    def test_supported_math(self):
        self.assertFalse(inspect('$x$ and $`y_1`$\n\n$$a=b$$\n\n```math\nc=d\n```')['errors'])
    def test_unclosed_inline(self):
        self.assertTrue(inspect('Text $x')['errors'])
    def test_unclosed_backtick_math(self):
        self.assertTrue(inspect('Text $`x$')['errors'])
    def test_unclosed_display(self):
        self.assertTrue(inspect('$$x')['errors'])
    def test_unclosed_fence(self):
        self.assertTrue(inspect('```math\nx')['errors'])
    def test_table_pipe(self):
        self.assertTrue(inspect('| A | B |\n|---|---|\n| X | $`|x|`$ |')['errors'])
    def test_safe_table(self):
        self.assertFalse(inspect('| A | B |\n|---|---|\n| X | $`\\lvert x\\rvert`$ |')['errors'])
    def test_grouping(self):
        self.assertTrue(inspect('$`x^{2`$')['errors'])
    def test_literal_braces(self):
        self.assertFalse(inspect(r'$`\{x\}`$')['errors'])
    def test_code_is_not_math(self):
        self.assertFalse(inspect('`$HOME`\n```sh\necho $X\n```')['errors'])
    def test_adjacent_inline_math(self):
        result = inspect('$`N`$ emitters and $`M`$ excitations.')
        self.assertFalse(result['errors'])
        self.assertEqual([e['tex'] for e in result['expressions']], ['N', 'M'])
    def test_injected_backtick(self):
        self.assertTrue(inspect('$`N`$` emitters and `$`M`$.')['errors'])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(PresentationTests))
        if not result.wasSuccessful():
            raise SystemExit(1)
    reports = []
    for path in sorted(args.root.rglob('*.md')):
        if any(p in {'.git', '.venv', 'node_modules', 'verification-artifacts'} for p in path.relative_to(args.root).parts):
            continue
        reports.append(inspect(path.read_text(encoding='utf-8'), str(path.relative_to(args.root))))
    errors = [e for report in reports for e in report['errors']]
    summary = dict(status='FAIL' if errors else 'PASS', markdown_files=len(reports),
                   math_expressions=sum(len(r['expressions']) for r in reports), files=reports,
                   scope='Markdown/TeX delimiter and table structure only; no rendering or scientific verification.')
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n')
    for error in errors:
        print(error, file=sys.stderr)
    print(f'{summary["status"]} presentation: {len(reports)} Markdown files; {summary["math_expressions"]} expressions')
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
