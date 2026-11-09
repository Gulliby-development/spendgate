<p align="center"><img src="docs/logo.svg" width="96" alt="" /></p>

# spendgate

[![CI](https://github.com/Gulliby-development/spendgate/actions/workflows/ci.yml/badge.svg)](https://github.com/Gulliby-development/spendgate/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

spendgate is a small, dependency-free command-line tool for validating token-usage records,
estimating their cost, and checking context-window and spending limits. It is intended for teams
that track language-model calls and want readable reports in a terminal, a script, or continuous
integration (CI). It uses a built-in price table; it makes no model calls and no network calls. See the [MIT license](LICENSE).

## Requirements and invocation

Use Python 3.11 or newer. From the repository directory, run:

```sh
python -m spendgate COMMAND
```

The runtime uses only the Python standard library. The commands below read usage records from
standard input where indicated; `models` does not read input. Windows, macOS, and Linux are
supported. The shell examples later in this guide use POSIX shell syntax.

## Commands

The synopsis is:

```text
usage: spendgate check
       spendgate models
       spendgate cost [--by model|line]
       spendgate fit [--pct N]
       spendgate budget --limit USD [--warn N]
```

The first word selects the command. `help`, `-h`, and `--help` as the first word print the
synopsis and exit successfully, regardless of later words. `--version` prints
`spendgate 0.1.0` and exits successfully. With no arguments, the synopsis is written to standard
error and the exit status is 2. A different first word is an unknown-command error.

Options are read from left to right. `cost` accepts `--by model` or `--by line` (default:
`model`); `fit` accepts `--pct N` (default: `100`); and `budget` requires `--limit USD`
and optionally accepts `--warn N`. `check` and `models` accept no options. Each option may
appear only once. An option's next word is its value, even if that word looks like an option.
For an option, validation checks duplicates first, then a missing value, then an invalid value.
A missing budget limit is reported after the supplied options have been checked.

`N` values are unsigned decimal integers written with ASCII digits, no sign, and no leading zero
(except `0` itself). Percent thresholds range from 1 through 1000 for `--pct`, and 1 through
100 for `--warn`. A USD limit is written as decimal digits with no leading zero, optionally
followed by a point and one to six digits: for example, `12`, `12.5`, and `0.000001`.
The limit range is 0.000001 through 1000000 inclusive. Exponential notation, commas, a leading
point, and a trailing point are not accepted.

Only a valid invocation of `check`, `cost`, `fit`, or `budget` reads standard input.
Invalid command lines fail before input is read. `models` ignores input.

## Usage-list input

Provide one call per line as `MODEL INPUT OUTPUT` or
`MODEL INPUT OUTPUT CACHED`. The five case-sensitive model names are `lark-s`, `lark-m`,
`lark-l`, `wren-s`, and `wren-xl`. Token counts are unsigned ASCII decimal integers with no
leading zero (other than `0`) and range from 0 through 1000000000 inclusive. `CACHED` is the
portion of input tokens served from cache; it defaults to zero and cannot exceed `INPUT`.

Lines are split at line feeds (LF); a final line without LF still counts, while empty input has no
lines. One carriage return (CR) at the end of a line is removed. Spaces and tabs separate fields
and are ignored at line ends. A blank line or a line whose first word begins with `#` is skipped.
No other character separates fields. The input is limited to 40 lines, including skipped lines;
this limit is checked before individual records are validated.

For each non-skipped record, validation proceeds in this order: field count, model name, input
count, output count, cached count, then whether cached exceeds input. The first error is reported
with its one-based input line number. All records are validated before a command reports results.
The `check` command prints `ok N record(s)`, counting calls but not skipped lines.
`models` prints the built-in table without validating or reading input.

## Built-in prices and context windows

Prices are US dollars per million tokens. Context is the combined input and output token window.

| Model | Input | Output | Cached input | Context window |
| --- | ---: | ---: | ---: | ---: |
| lark-s | $0.20 | $0.80 | $0.02 | 128000 |
| lark-m | $1.50 | $6.00 | $0.15 | 200000 |
| lark-l | $6.00 | $24.00 | $0.60 | 200000 |
| wren-s | $0.10 | $0.40 | $0.01 | 32000 |
| wren-xl | $12.00 | $48.00 | $1.20 | 1000000 |

## Reports and exit statuses

Successful commands write their reports to standard output and nothing to standard error. A
command-line or invalid-input failure writes no standard output and one error line to standard
error; command-line errors exit with status 2 and invalid usage input exits with status 1. An
exceeded `fit` or `budget` gate is different: it keeps its report on standard output, writes
nothing to standard error, and exits with status 1. Otherwise, both gate commands exit with status 0.

- **`check`** validates all records and prints `ok N record(s)`. Empty input prints
  `ok 0 records`; a single call prints `ok 1 record`.
- **`models`** prints one line per model in the table's order, formatted as
  `NAME in P out P cached P context W`. Prices have two decimal places. It never reads input.
- **`cost`** reports exact costs by model, in each model's first-occurrence order, or by input
  line, in input order (use `--by line`). Model rows include call counts and summed input,
  output, and cached tokens. Line rows retain the original, one-based line numbers, including
  skipped lines. Both modes finish with `total N records AMOUNT`; empty input therefore prints
  `total 0 records $0.000000`. Model rows use `MODEL N records in I out O cached C AMOUNT`;
  line rows use `line N MODEL AMOUNT`.
- **`fit`** lists each call whose input plus output is strictly greater than the selected
  percentage of its model's context window. Cached tokens still count toward context. Each
  listed line includes its original line number, token total, window, and share; the final line
  is `over K of N records`. A listed call uses the form
  `line N MODEL uses T of W tokens (S%)`. It exits 1 if any call is listed, otherwise 0.
- **`budget`** prints `spent AMOUNT of LIMIT (S%)`, then one outcome. An exact total greater
  than the limit prints `over by AMOUNT` and exits 1. Otherwise, when `--warn` is present and
  the exact total is at least that percentage of the limit, it prints
  `warning: at or above W% of the limit` and exits 0. The warning threshold is inclusive, but
  an over-limit result takes precedence. All other totals print `within the limit` and exit 0.

For each call, the exact cost is calculated per million tokens: charge `INPUT` minus `CACHED`
at the input price, `CACHED` at the cached-input price, and `OUTPUT` at the output price, then
add those charges. Cached tokens therefore replace the ordinary input charge for that portion; they
do not add a second charge. Costs use integer arithmetic, not floating point. Each reported amount
(a call, model group, total, limit, or difference) is rounded independently from its exact value to
six decimal places, half up. Consequently, separately rounded call amounts need not sum to the
rounded total. Shares are rounded independently to one decimal place, half up. Counts use a singular
noun only for one (for example, `1 record`, `2 records`, and `0 records`).

### Error messages

Every error is prefixed with `spendgate: `. Command-line errors use these exact forms:

- `unknown command WORD`
- `unexpected argument WORD`
- `unknown option WORD`
- `option OPTION is not valid for COMMAND`
- `given twice: OPTION`
- `missing value for OPTION`
- `bad value for OPTION`
- `missing --limit`

Input errors use these exact forms:

- `input is too long (max 40 lines)`
- `line N: expected MODEL INPUT OUTPUT [CACHED]`
- `line N: unknown model WORD`
- `line N: bad input WORD`
- `line N: bad output WORD`
- `line N: bad cached WORD`
- `line N: cached exceeds input`

Here, `WORD`, `OPTION`, `COMMAND`, and `N` are replaced by the offending value, command,
option, or one-based line number. Error text includes the offending input word as read, including
non-ASCII characters or a residual CR when present.

## Examples

In the examples below, `spendgate` stands for `python -m spendgate`. The commands are shown
for a POSIX shell in the repository directory. The `2>&1` redirection sends standard error to
standard output so the validation errors are visible alongside other output.

```text
$ printf 'lark-m 12000 800 4000\nwren-s 3000 500\n' | spendgate cost
lark-m 1 record in 12000 out 800 cached 4000 $0.017400
wren-s 1 record in 3000 out 500 cached 0 $0.000500
total 2 records $0.017900
$ printf 'lark-m 12000 800 4000\nwren-s 3000 500\n' | spendgate cost --by line
line 1 lark-m $0.017400
line 2 wren-s $0.000500
total 2 records $0.017900
$ printf 'lark-m 12000 800 4000\nwren-s 30000 5000\n' | spendgate fit --pct 50; printf 'lark-m 12000 800 4000\nwren-s 3000 500\n' | spendgate budget --limit 0.02 --warn 80
line 2 wren-s uses 35000 of 32000 tokens (109.4%)
over 1 of 2 records
spent $0.017900 of $0.020000 (89.5%)
warning: at or above 80% of the limit
$ printf 'lark-s 1 x\n' | spendgate check 2>&1; printf 'lark-s 5 1 6\n' | spendgate cost 2>&1
spendgate: line 1: bad output x
spendgate: line 1: cached exceeds input
```

## Development

Install the development tools listed in `requirements-dev.txt` in your environment. They are
for checks only; spendgate itself has no third-party runtime dependencies. From the repository
directory, run:

```sh
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
```

The tests exercise command behavior through the command-line interface helpers.

---

Built with [BAKED](https://github.com/Gulliby-development/baked), an open-source coding agent (bench round R98).
