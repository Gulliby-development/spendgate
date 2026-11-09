"""Command-line parsing, stdin gating and command dispatch."""

import importlib
import re

from spendgate.records import read_records
from spendgate.registry import (
    COMMAND_TABLE,
    MAX_LIMIT_MICRO,
    MAX_PCT,
    MAX_WARN,
    OPTION_NAMES,
    USAGE,
    VERSION,
    Failure,
    fail,
    reply,
)

_UNSIGNED = re.compile(r"(?:0|[1-9][0-9]*)\Z", re.ASCII)
_LIMIT = re.compile(r"(?:0|[1-9][0-9]*)(?:\.[0-9]{1,6})?\Z", re.ASCII)
_COMMANDS = {name: (module, options) for name, module, options in COMMAND_TABLE}


def _parse_limit(value):
    """Parse a canonical dollar amount as integer micro-dollars."""
    if not _LIMIT.fullmatch(value):
        return None
    whole, separator, fraction = value.partition(".")
    micros_text = whole + (fraction.ljust(6, "0") if separator else "000000")
    if len(micros_text) > len(str(MAX_LIMIT_MICRO)) or (
        len(micros_text) == len(str(MAX_LIMIT_MICRO)) and micros_text > str(MAX_LIMIT_MICRO)
    ):
        return None
    amount = int(micros_text)
    return amount if amount >= 1 else None


def _parse_options(args):
    """Validate a command line and return its command and normalized options."""
    if not args:
        fail(2, "missing command")
    command = args[0]
    if command not in _COMMANDS:
        fail(2, f"unknown command {command}")

    _module, accepted = _COMMANDS[command]
    options = {"by": "model", "pct": 100}
    seen = set()
    index = 1
    while index < len(args):
        word = args[index]
        if not word or word == "-" or not word.startswith("-"):
            fail(2, f"unexpected argument {word}")
        if word not in OPTION_NAMES:
            fail(2, f"unknown option {word}")
        if word not in accepted:
            fail(2, f"option {word} is not valid for {command}")
        if word in seen:
            fail(2, f"given twice: {word}")
        seen.add(word)
        if index + 1 >= len(args):
            fail(2, f"missing value for {word}")
        value = args[index + 1]
        if word == "--by":
            if value not in ("model", "line"):
                fail(2, f"bad value for {word}")
            options["by"] = value
        elif word in ("--pct", "--warn"):
            maximum = MAX_PCT if word == "--pct" else MAX_WARN
            if not _UNSIGNED.fullmatch(value):
                fail(2, f"bad value for {word}")
            if len(value) > len(str(maximum)) or (
                len(value) == len(str(maximum)) and value > str(maximum)
            ):
                fail(2, f"bad value for {word}")
            number = int(value)
            if number < 1:
                fail(2, f"bad value for {word}")
            options["pct" if word == "--pct" else "warn"] = number
        else:
            amount = _parse_limit(value)
            if amount is None:
                fail(2, f"bad value for {word}")
            options["limit"] = amount
        index += 2
    if command == "budget" and "--limit" not in seen:
        fail(2, "missing --limit")
    return command, _COMMANDS[command][0], options


def reads_stdin(args):
    """Return whether a valid command line consumes usage input."""
    try:
        command, _module, _options = _parse_options(args)
    except Failure:
        return False
    return command in ("check", "cost", "fit", "budget")


def run_cli(args, text):
    """Validate arguments and input, then return the selected command's reply."""
    if not args:
        return reply(2, "", USAGE)
    if args[0] in ("help", "-h", "--help"):
        return reply(0, USAGE, "")
    if args and args[0] == "--version":
        return reply(0, f"spendgate {VERSION}\n", "")
    try:
        command, module_name, options = _parse_options(args)
        if command == "models":
            records = []
        else:
            records = read_records(text)
        module = importlib.import_module(module_name)
        return module.run(options, records)
    except Failure as failure:
        return reply(failure.status, "", f"spendgate: {failure.message}\n")
