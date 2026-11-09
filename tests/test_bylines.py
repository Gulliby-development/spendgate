from harness import row, rows_test

# fmt: off
ROWS = [
    row(["cost", "--by", "line"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "line 1 lark-s $0.000360\nline 2 lark-m $0.005400\nline 3 wren-s $0.005000\ntotal 3 records $0.010760\n", ""),
    row(["cost", "--by", "line"], "lark-m 100 10\nlark-s 200 20 50\nlark-m 300 30\nwren-xl 1000000 5000 1000\nlark-s 1 1\n", 0, "line 1 lark-m $0.000210\nline 2 lark-s $0.000047\nline 3 lark-m $0.000630\nline 4 wren-xl $12.229200\nline 5 lark-s $0.000001\ntotal 5 records $12.230088\n", ""),
    row(["cost", "--by", "line"], "# c\n\nwren-s 10 10\n\nlark-s 1000000 1\n", 0, "line 3 wren-s $0.000005\nline 5 lark-s $0.200001\ntotal 2 records $0.200006\n", ""),
    row(["cost", "--by", "line"], "lark-s 1 1\n", 0, "line 1 lark-s $0.000001\ntotal 1 record $0.000001\n", ""),
    row(["cost", "--by", "line"], "lark-l 123456 7890 1234\n", 0, "line 1 lark-l $0.923432\ntotal 1 record $0.923432\n", ""),
    row(["cost"], "lark-l 123456 7890 1234\nlark-l 654321 9876 54321\n", 0, "lark-l 2 records in 777777 out 17766 cached 55555 $4.793049\ntotal 2 records $4.793049\n", ""),
    row(["cost"], "wren-xl 999999999 999999999 999999999\nwren-xl 1 1\n", 0, "wren-xl 2 records in 1000000000 out 1000000000 cached 999999999 $49200.000011\ntotal 2 records $49200.000011\n", ""),
    row(["cost"], "lark-s 3 0\n", 0, "lark-s 1 record in 3 out 0 cached 0 $0.000001\ntotal 1 record $0.000001\n", ""),
    row(["cost", "--by", "line"], "lark-s 3 0\nlark-s 3 0\nlark-s 3 0\nlark-s 3 0\n", 0, "line 1 lark-s $0.000001\nline 2 lark-s $0.000001\nline 3 lark-s $0.000001\nline 4 lark-s $0.000001\ntotal 4 records $0.000002\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
