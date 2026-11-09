from harness import row, rows_test

# fmt: off
ROWS = [
    row(["fit", "--pct", "0"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --pct\n"),
    row(["fit", "--pct", "1001"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --pct\n"),
    row(["fit", "--pct", "007"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --pct\n"),
    row(["fit", "--pct", "\u0663"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --pct\n"),
    row(["budget", "--limit", "0"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --limit\n"),
    row(["budget", "--limit", "0.0000001"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --limit\n"),
    row(["budget", "--limit", "1000000.000001"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --limit\n"),
    row(["budget", "--limit", "01"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --limit\n"),
    row(["budget", "--limit", "5."], "lark-s 1 1\n", 2, "", "spendgate: bad value for --limit\n"),
    row(["budget", "--limit", "1", "--warn", "0"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --warn\n"),
    row(["budget", "--limit", "1", "--warn", "101"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --warn\n"),
    row(["check"], "wren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\n", 1, "", "spendgate: input is too long (max 40 lines)\n"),
    row(["check"], "frob\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\n", 1, "", "spendgate: input is too long (max 40 lines)\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
