from harness import row, rows_test

# fmt: off
ROWS = [
    row(["check"], "wren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\n", 0, "ok 40 records\n", ""),
    row(["check"], "lark-s 1000000000 1000000000 1000000000\n", 0, "ok 1 record\n", ""),
    row(["check"], "lark-s 1000000001 1\n", 1, "", "spendgate: line 1: bad input 1000000001\n"),
    row(["check"], "lark-s 1 1000000001\n", 1, "", "spendgate: line 1: bad output 1000000001\n"),
    row(["cost"], "wren-xl 1000000000 1000000000 1000000000\n", 0, "wren-xl 1 record in 1000000000 out 1000000000 cached 1000000000 $49200.000000\ntotal 1 record $49200.000000\n", ""),
    row(["fit", "--pct", "1"], "# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\nwren-s 321 0\n", 1, "line 40 wren-s uses 321 of 32000 tokens (1.0%)\nover 1 of 1 record\n", ""),
    row(["budget", "--limit", "1000000"], "# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\n# c\nwren-xl 1000000000 1000000000\n", 0, "spent $60000.000000 of $1000000.000000 (6.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "0.000001"], "", 0, "spent $0.000000 of $0.000001 (0.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "1000000", "--warn", "100"], "wren-xl 1000000000 1000000000\n", 0, "spent $60000.000000 of $1000000.000000 (6.0%)\nwithin the limit\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
