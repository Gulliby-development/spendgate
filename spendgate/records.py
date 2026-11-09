"""Parse and validate ordered usage records."""

import re

from spendgate.registry import MAX_LINES, MAX_TOKENS, MODELS, fail

_MODEL_NAMES = {model[0] for model in MODELS}
_UNSIGNED_INTEGER = re.compile(r"(?:0|[1-9][0-9]*)\Z", re.ASCII)


def _parse_token(token, field, line_number):
    """Return a bounded canonical token count, or fail with its field-specific error."""
    if not _UNSIGNED_INTEGER.fullmatch(token):
        fail(1, f"line {line_number}: bad {field} {token}")
    if len(token) > len(str(MAX_TOKENS)) or (
        len(token) == len(str(MAX_TOKENS)) and token > str(MAX_TOKENS)
    ):
        fail(1, f"line {line_number}: bad {field} {token}")
    return int(token)


def read_records(text):
    """Validate input text and return records in their original line order."""
    if not text:
        lines = []
    else:
        lines = text.split("\n")
        if text.endswith("\n"):
            lines.pop()

    if len(lines) > MAX_LINES:
        fail(1, f"input is too long (max {MAX_LINES} lines)")

    records = []
    for line_number, line in enumerate(lines, start=1):
        if line.endswith("\r"):
            line = line[:-1]
        words = re.split(r"[ \t]+", line.strip(" \t"))
        if words == [""] or words[0].startswith("#"):
            continue
        if len(words) not in (3, 4):
            fail(1, f"line {line_number}: expected MODEL INPUT OUTPUT [CACHED]")

        model, input_text, output_text = words[:3]
        cached_text = words[3] if len(words) == 4 else "0"
        if model not in _MODEL_NAMES:
            fail(1, f"line {line_number}: unknown model {model}")
        input_count = _parse_token(input_text, "input", line_number)
        output_count = _parse_token(output_text, "output", line_number)
        cached_count = _parse_token(cached_text, "cached", line_number)
        if cached_count > input_count:
            fail(1, f"line {line_number}: cached exceeds input")
        records.append(
            {
                "line": line_number,
                "model": model,
                "input": input_count,
                "output": output_count,
                "cached": cached_count,
            }
        )
    return records
