from harness import row, rows_test

# fmt: off
ROWS = [
    row(["cost"], "", 0, "total 0 records $0.000000\n", ""),
    row(["cost"], "lark-s 1000000 1000000 1000000\n", 0, "lark-s 1 record in 1000000 out 1000000 cached 1000000 $0.820000\ntotal 1 record $0.820000\n", ""),
    row(["cost"], "lark-m 1000000 1000000\n", 0, "lark-m 1 record in 1000000 out 1000000 cached 0 $7.500000\ntotal 1 record $7.500000\n", ""),
    row(["cost"], "lark-l 1000000 1000000 500000\n", 0, "lark-l 1 record in 1000000 out 1000000 cached 500000 $27.300000\ntotal 1 record $27.300000\n", ""),
    row(["cost"], "wren-s 1000000 1000000\n", 0, "wren-s 1 record in 1000000 out 1000000 cached 0 $0.500000\ntotal 1 record $0.500000\n", ""),
    row(["cost"], "wren-xl 1000000 1000000 250000\n", 0, "wren-xl 1 record in 1000000 out 1000000 cached 250000 $57.300000\ntotal 1 record $57.300000\n", ""),
    row(["cost"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "lark-s 1 record in 1000 out 200 cached 0 $0.000360\nlark-m 1 record in 5000 out 100 cached 2000 $0.005400\nwren-s 1 record in 30000 out 5000 cached 0 $0.005000\ntotal 3 records $0.010760\n", ""),
    row(["cost"], "lark-m 100 10\nlark-s 200 20 50\nlark-m 300 30\nwren-xl 1000000 5000 1000\nlark-s 1 1\n", 0, "lark-m 2 records in 400 out 40 cached 0 $0.000840\nlark-s 2 records in 201 out 21 cached 50 $0.000048\nwren-xl 1 record in 1000000 out 5000 cached 1000 $12.229200\ntotal 5 records $12.230088\n", ""),
    row(["cost"], "lark-s 1 1\nlark-s 2 2\nlark-s 3 3\n", 0, "lark-s 3 records in 6 out 6 cached 0 $0.000006\ntotal 3 records $0.000006\n", ""),
    row(["cost"], "lark-m 1 1\nlark-s 1 1\nlark-m 1 1\nlark-s 1 1\n", 0, "lark-m 2 records in 2 out 2 cached 0 $0.000015\nlark-s 2 records in 2 out 2 cached 0 $0.000002\ntotal 4 records $0.000017\n", ""),
    row(["cost"], "# c\n\nwren-s 10 10\n\n# d\n", 0, "wren-s 1 record in 10 out 10 cached 0 $0.000005\ntotal 1 record $0.000005\n", ""),
    row(["cost"], "wren-s 7 0 7\nwren-xl 7 0 7\n", 0, "wren-s 1 record in 7 out 0 cached 7 $0.000000\nwren-xl 1 record in 7 out 0 cached 7 $0.000008\ntotal 2 records $0.000008\n", ""),
    row(["cost"], "lark-m 2 2\r\nlark-m 2 2\r\n", 0, "lark-m 2 records in 4 out 4 cached 0 $0.000030\ntotal 2 records $0.000030\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
