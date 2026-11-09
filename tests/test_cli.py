from harness import row, rows_test

# fmt: off
ROWS = [
    row(["frob"], "", 2, "", "spendgate: unknown command frob\n"),
    row([""], "", 2, "", "spendgate: unknown command \n"),
    row(["Check"], "", 2, "", "spendgate: unknown command Check\n"),
    row(["check"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "ok 3 records\n", ""),
    row(["models"], "", 0, "lark-s in 0.20 out 0.80 cached 0.02 context 128000\nlark-m in 1.50 out 6.00 cached 0.15 context 200000\nlark-l in 6.00 out 24.00 cached 0.60 context 200000\nwren-s in 0.10 out 0.40 cached 0.01 context 32000\nwren-xl in 12.00 out 48.00 cached 1.20 context 1000000\n", ""),
    row(["check", "x"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 2, "", "spendgate: unexpected argument x\n"),
    row(["check"], "frob 1 2\n", 1, "", "spendgate: line 1: unknown model frob\n"),
    row(["budget"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 2, "", "spendgate: missing --limit\n"),
    row(["cost"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "lark-s 1 record in 1000 out 200 cached 0 $0.000360\nlark-m 1 record in 5000 out 100 cached 2000 $0.005400\nwren-s 1 record in 30000 out 5000 cached 0 $0.005000\ntotal 3 records $0.010760\n", ""),
    row(["cost", "--by", "line"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "line 1 lark-s $0.000360\nline 2 lark-m $0.005400\nline 3 wren-s $0.005000\ntotal 3 records $0.010760\n", ""),
    row(["fit"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 1, "line 3 wren-s uses 35000 of 32000 tokens (109.4%)\nover 1 of 3 records\n", ""),
    row(["budget", "--limit", "0.01"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 1, "spent $0.010760 of $0.010000 (107.6%)\nover by $0.000760\n", ""),
    row(["budget", "--limit", "1"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "spent $0.010760 of $1.000000 (1.1%)\nwithin the limit\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
