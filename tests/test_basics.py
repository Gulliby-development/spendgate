from harness import row, rows_test

# fmt: off
ROWS = [
    row(["check"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "ok 3 records\n", ""),
    row(["check"], "lark-s 0 0\n", 0, "ok 1 record\n", ""),
    row(["check"], "lark-s 7 7 7\n", 0, "ok 1 record\n", ""),
    row(["check"], "# a\n\nlark-m 1 2\n  \n# b\nwren-xl 3 4 1\n", 0, "ok 2 records\n", ""),
    row(["check"], "wren-s 1000000000 1000000000 1000000000\n", 0, "ok 1 record\n", ""),
    row(["check"], "lark-m 100 10\nlark-s 200 20 50\nlark-m 300 30\nwren-xl 1000000 5000 1000\nlark-s 1 1\n", 0, "ok 5 records\n", ""),
    row(["check"], "lark-l 1 1\r\nlark-l 2 2\r\n", 0, "ok 2 records\n", ""),
    row(["check"], "lark-s 1 1\n\n\n", 0, "ok 1 record\n", ""),
    row(["models"], "", 0, "lark-s in 0.20 out 0.80 cached 0.02 context 128000\nlark-m in 1.50 out 6.00 cached 0.15 context 200000\nlark-l in 6.00 out 24.00 cached 0.60 context 200000\nwren-s in 0.10 out 0.40 cached 0.01 context 32000\nwren-xl in 12.00 out 48.00 cached 1.20 context 1000000\n", ""),
    row(["models"], "frob\n", 0, "lark-s in 0.20 out 0.80 cached 0.02 context 128000\nlark-m in 1.50 out 6.00 cached 0.15 context 200000\nlark-l in 6.00 out 24.00 cached 0.60 context 200000\nwren-s in 0.10 out 0.40 cached 0.01 context 32000\nwren-xl in 12.00 out 48.00 cached 1.20 context 1000000\n", ""),
    row(["models"], "wren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\nwren-s 1 1\n", 0, "lark-s in 0.20 out 0.80 cached 0.02 context 128000\nlark-m in 1.50 out 6.00 cached 0.15 context 200000\nlark-l in 6.00 out 24.00 cached 0.60 context 200000\nwren-s in 0.10 out 0.40 cached 0.01 context 32000\nwren-xl in 12.00 out 48.00 cached 1.20 context 1000000\n", ""),
    row(["models", "x"], "", 2, "", "spendgate: unexpected argument x\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
