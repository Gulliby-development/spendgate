from harness import row, rows_test

# fmt: off
ROWS = [
    row(["budget", "--limit", "1"], "", 0, "spent $0.000000 of $1.000000 (0.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "1"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "spent $0.010760 of $1.000000 (1.1%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "0.01076"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "spent $0.010760 of $0.010760 (100.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "0.010759"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 1, "spent $0.010760 of $0.010759 (100.0%)\nover by $0.000001\n", ""),
    row(["budget", "--limit", "0.01"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 1, "spent $0.010760 of $0.010000 (107.6%)\nover by $0.000760\n", ""),
    row(["budget", "--limit", "0.5"], "lark-s 1000000 0\n", 0, "spent $0.200000 of $0.500000 (40.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "0.19"], "lark-s 1000000 0\n", 1, "spent $0.200000 of $0.190000 (105.3%)\nover by $0.010000\n", ""),
    row(["budget", "--limit", "12.345678"], "lark-m 100 10\nlark-s 200 20 50\nlark-m 300 30\nwren-xl 1000000 5000 1000\nlark-s 1 1\n", 0, "spent $12.230088 of $12.345678 (99.1%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "100"], "wren-xl 1000000 1000000\n", 0, "spent $60.000000 of $100.000000 (60.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "0.000001"], "wren-s 10 0\n", 0, "spent $0.000001 of $0.000001 (100.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "0.000001"], "wren-s 11 0\n", 1, "spent $0.000001 of $0.000001 (110.0%)\nover by $0.000000\n", ""),
    row(["budget", "--limit", "0.000001"], "wren-s 5 0\n", 0, "spent $0.000001 of $0.000001 (50.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "1000000"], "wren-xl 1 1\n", 0, "spent $0.000060 of $1000000.000000 (0.0%)\nwithin the limit\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
