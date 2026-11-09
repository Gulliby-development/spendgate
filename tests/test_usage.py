from harness import row, rows_test

# fmt: off
ROWS = [
    row([], "", 2, "", "usage: spendgate check\n       spendgate models\n       spendgate cost [--by model|line]\n       spendgate fit [--pct N]\n       spendgate budget --limit USD [--warn N]\n"),
    row(["help"], "", 0, "usage: spendgate check\n       spendgate models\n       spendgate cost [--by model|line]\n       spendgate fit [--pct N]\n       spendgate budget --limit USD [--warn N]\n", ""),
    row(["-h"], "", 0, "usage: spendgate check\n       spendgate models\n       spendgate cost [--by model|line]\n       spendgate fit [--pct N]\n       spendgate budget --limit USD [--warn N]\n", ""),
    row(["--help", "frob"], "ignored\n", 0, "usage: spendgate check\n       spendgate models\n       spendgate cost [--by model|line]\n       spendgate fit [--pct N]\n       spendgate budget --limit USD [--warn N]\n", ""),
    row(["--version"], "", 0, "spendgate 0.1.0\n", ""),
    row(["--version", "x"], "", 0, "spendgate 0.1.0\n", ""),
    row(["check", "--by", "line"], "lark-s 1 1\n", 2, "", "spendgate: option --by is not valid for check\n"),
    row(["models", "--limit", "1"], "", 2, "", "spendgate: option --limit is not valid for models\n"),
    row(["cost", "--pct", "5"], "lark-s 1 1\n", 2, "", "spendgate: option --pct is not valid for cost\n"),
    row(["fit", "--by", "line"], "lark-s 1 1\n", 2, "", "spendgate: option --by is not valid for fit\n"),
    row(["budget", "--by", "line"], "lark-s 1 1\n", 2, "", "spendgate: option --by is not valid for budget\n"),
    row(["budget", "--pct", "5", "--limit", "1"], "lark-s 1 1\n", 2, "", "spendgate: option --pct is not valid for budget\n"),
    row(["cost", "--nope"], "lark-s 1 1\n", 2, "", "spendgate: unknown option --nope\n"),
    row(["cost", "-"], "lark-s 1 1\n", 2, "", "spendgate: unexpected argument -\n"),
    row(["cost", "extra"], "lark-s 1 1\n", 2, "", "spendgate: unexpected argument extra\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
