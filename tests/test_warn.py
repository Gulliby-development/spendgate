from harness import row, rows_test

# fmt: off
ROWS = [
    row(["budget", "--limit", "1", "--warn", "50"], "lark-s 2500000 0\n", 0, "spent $0.500000 of $1.000000 (50.0%)\nwarning: at or above 50% of the limit\n", ""),
    row(["budget", "--limit", "1", "--warn", "50"], "lark-s 2000000 0\n", 0, "spent $0.400000 of $1.000000 (40.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "1", "--warn", "50"], "lark-s 2499999 0\n", 0, "spent $0.500000 of $1.000000 (50.0%)\nwithin the limit\n", ""),
    row(["budget", "--limit", "1", "--warn", "100"], "lark-s 5000000 0\n", 0, "spent $1.000000 of $1.000000 (100.0%)\nwarning: at or above 100% of the limit\n", ""),
    row(["budget", "--limit", "1", "--warn", "100"], "lark-s 5000001 0\n", 1, "spent $1.000000 of $1.000000 (100.0%)\nover by $0.000000\n", ""),
    row(["budget", "--limit", "1", "--warn", "1"], "lark-s 50000 0\n", 0, "spent $0.010000 of $1.000000 (1.0%)\nwarning: at or above 1% of the limit\n", ""),
    row(["budget", "--warn", "80", "--limit", "1"], "lark-s 4000000 0\n", 0, "spent $0.800000 of $1.000000 (80.0%)\nwarning: at or above 80% of the limit\n", ""),
    row(["budget", "--limit", "5", "--warn", "20"], "lark-m 1000000 1000000\n", 1, "spent $7.500000 of $5.000000 (150.0%)\nover by $2.500000\n", ""),
    row(["budget", "--limit", "7.5", "--warn", "100"], "lark-m 1000000 1000000\n", 0, "spent $7.500000 of $7.500000 (100.0%)\nwarning: at or above 100% of the limit\n", ""),
    row(["budget", "--limit", "0.000001", "--warn", "100"], "wren-s 10 0\n", 0, "spent $0.000001 of $0.000001 (100.0%)\nwarning: at or above 100% of the limit\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
