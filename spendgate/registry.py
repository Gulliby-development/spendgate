"""Shared constants and helpers of spendgate: the version, the limits, the price table, the usage text, the command table, fail() and reply()."""

VERSION = "0.1.0"
MAX_LINES = 40
MAX_TOKENS = 1000000000
MAX_PCT = 1000
MAX_WARN = 100
MAX_LIMIT_MICRO = 1000000000000

# One row per model: its name, then the prices in hundredths of a US dollar per million tokens
# (input, output, cached input) and the context window in tokens. One token at 20 hundredths costs 200 nano-dollars.
MODELS = (
    ("lark-s", 20, 80, 2, 128000),
    ("lark-m", 150, 600, 15, 200000),
    ("lark-l", 600, 2400, 60, 200000),
    ("wren-s", 10, 40, 1, 32000),
    ("wren-xl", 1200, 4800, 120, 1000000),
)

USAGE = (
    "usage: spendgate check\n"
    "       spendgate models\n"
    "       spendgate cost [--by model|line]\n"
    "       spendgate fit [--pct N]\n"
    "       spendgate budget --limit USD [--warn N]\n"
)

# One entry per command: its word, the module that holds it and the options that it accepts.
COMMAND_TABLE = (
    ("check", "spendgate.cmd_check", ()),
    ("models", "spendgate.cmd_models", ()),
    ("cost", "spendgate.cmd_cost", ("--by",)),
    ("fit", "spendgate.cmd_fit", ("--pct",)),
    ("budget", "spendgate.cmd_budget", ("--limit", "--warn")),
)

OPTION_NAMES = ("--by", "--pct", "--limit", "--warn")


class Failure(Exception):
    """A failure that ends the command: status 1 for the input, 2 for the command line."""

    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


def fail(status, message):
    raise Failure(status, message)


def reply(status, out, err):
    return {"status": status, "out": out, "err": err}
