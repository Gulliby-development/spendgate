from harness import row, rows_test

# fmt: off
ROWS = [
    row(["fit"], "", 0, "over 0 of 0 records\n", ""),
    row(["fit"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 1, "line 3 wren-s uses 35000 of 32000 tokens (109.4%)\nover 1 of 3 records\n", ""),
    row(["fit"], "wren-s 32000 0\n", 0, "over 0 of 1 record\n", ""),
    row(["fit"], "wren-s 32000 1\n", 1, "line 1 wren-s uses 32001 of 32000 tokens (100.0%)\nover 1 of 1 record\n", ""),
    row(["fit"], "wren-s 16000 16000\n", 0, "over 0 of 1 record\n", ""),
    row(["fit"], "lark-s 100000 28001\n", 1, "line 1 lark-s uses 128001 of 128000 tokens (100.0%)\nover 1 of 1 record\n", ""),
    row(["fit"], "lark-m 150000 50001\nlark-l 150000 50000\n", 1, "line 1 lark-m uses 200001 of 200000 tokens (100.0%)\nover 1 of 2 records\n", ""),
    row(["fit"], "wren-xl 1000000 1\nwren-xl 999999 1\n", 1, "line 1 wren-xl uses 1000001 of 1000000 tokens (100.0%)\nover 1 of 2 records\n", ""),
    row(["fit"], "lark-s 128001 0 128001\n", 1, "line 1 lark-s uses 128001 of 128000 tokens (100.0%)\nover 1 of 1 record\n", ""),
    row(["fit", "--pct", "50"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 1, "line 3 wren-s uses 35000 of 32000 tokens (109.4%)\nover 1 of 3 records\n", ""),
    row(["fit", "--pct", "50"], "lark-s 64000 0\nlark-s 64001 0\n", 1, "line 2 lark-s uses 64001 of 128000 tokens (50.0%)\nover 1 of 2 records\n", ""),
    row(["fit", "--pct", "1"], "wren-s 321 0\nwren-s 320 0\n", 1, "line 1 wren-s uses 321 of 32000 tokens (1.0%)\nover 1 of 2 records\n", ""),
    row(["fit", "--pct", "1000"], "wren-s 320000 0\nwren-s 320001 0\n", 1, "line 2 wren-s uses 320001 of 32000 tokens (1000.0%)\nover 1 of 2 records\n", ""),
    row(["fit", "--pct", "10"], "lark-m 100 10\nlark-s 200 20 50\nlark-m 300 30\nwren-xl 1000000 5000 1000\nlark-s 1 1\n", 1, "line 4 wren-xl uses 1005000 of 1000000 tokens (100.5%)\nover 1 of 5 records\n", ""),
    row(["fit", "--pct", "100"], "# c\n\nwren-s 40000 0\n\nlark-s 1 1\nwren-s 50000 10\n", 1, "line 3 wren-s uses 40000 of 32000 tokens (125.0%)\nline 6 wren-s uses 50010 of 32000 tokens (156.3%)\nover 2 of 3 records\n", ""),
    row(["fit"], "wren-s 1000000000 1000000000\n", 1, "line 1 wren-s uses 2000000000 of 32000 tokens (6250000.0%)\nover 1 of 1 record\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
