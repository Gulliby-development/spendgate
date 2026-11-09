from harness import row, rows_test

# fmt: off
ROWS = [
    row(["cost"], "wren-s 5 0\n", 0, "wren-s 1 record in 5 out 0 cached 0 $0.000001\ntotal 1 record $0.000001\n", ""),
    row(["cost"], "wren-s 4 0\n", 0, "wren-s 1 record in 4 out 0 cached 0 $0.000000\ntotal 1 record $0.000000\n", ""),
    row(["cost"], "lark-s 0 1\n", 0, "lark-s 1 record in 0 out 1 cached 0 $0.000001\ntotal 1 record $0.000001\n", ""),
    row(["cost"], "lark-s 0 6\n", 0, "lark-s 1 record in 0 out 6 cached 0 $0.000005\ntotal 1 record $0.000005\n", ""),
    row(["cost", "--by", "line"], "wren-s 4 0\nwren-s 4 0\nwren-s 4 0\nwren-s 4 0\n", 0, "line 1 wren-s $0.000000\nline 2 wren-s $0.000000\nline 3 wren-s $0.000000\nline 4 wren-s $0.000000\ntotal 4 records $0.000002\n", ""),
    row(["cost", "--by", "line"], "wren-s 5 0\nwren-s 5 0\nwren-s 5 0\nwren-s 5 0\n", 0, "line 1 wren-s $0.000001\nline 2 wren-s $0.000001\nline 3 wren-s $0.000001\nline 4 wren-s $0.000001\ntotal 4 records $0.000002\n", ""),
    row(["cost"], "wren-xl 1 1\nwren-s 1 1\n", 0, "wren-xl 1 record in 1 out 1 cached 0 $0.000060\nwren-s 1 record in 1 out 1 cached 0 $0.000001\ntotal 2 records $0.000061\n", ""),
    row(["fit", "--pct", "1"], "wren-s 3 0\nwren-s 16 0\nwren-s 48 0\nwren-s 80 0\n", 0, "over 0 of 4 records\n", ""),
    row(["fit", "--pct", "1"], "lark-s 1281 0\nlark-s 1409 0\nlark-s 1537 0\n", 1, "line 1 lark-s uses 1281 of 128000 tokens (1.0%)\nline 2 lark-s uses 1409 of 128000 tokens (1.1%)\nline 3 lark-s uses 1537 of 128000 tokens (1.2%)\nover 3 of 3 records\n", ""),
    row(["fit", "--pct", "1"], "wren-xl 10001 0\nwren-xl 10005 0\nwren-xl 10004 0\n", 1, "line 1 wren-xl uses 10001 of 1000000 tokens (1.0%)\nline 2 wren-xl uses 10005 of 1000000 tokens (1.0%)\nline 3 wren-xl uses 10004 of 1000000 tokens (1.0%)\nover 3 of 3 records\n", ""),
    row(["budget", "--limit", "0.000008"], "wren-s 1 0\n", 0, "spent $0.000000 of $0.000008 (1.3%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "0.000004"], "wren-s 5 0\n", 0, "spent $0.000001 of $0.000004 (12.5%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "8"], "lark-s 5000000 1000000\n", 0, "spent $1.800000 of $8.000000 (22.5%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "0.000007"], "wren-s 4 0\nwren-s 4 0\nwren-s 4 0\nwren-s 4 0\n", 0, "spent $0.000002 of $0.000007 (22.9%)\nwithin the limit\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
