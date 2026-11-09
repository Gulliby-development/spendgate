from harness import row, rows_test

# fmt: off
ROWS = [
    row(["cost", ""], "lark-s 1 1\n", 2, "", "spendgate: unexpected argument \n"),
    row(["cost", "--by", "line", "--by", "model"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 2, "", "spendgate: given twice: --by\n"),
    row(["fit", "--pct", "5", "--pct", "bad"], "lark-s 1 1\n", 2, "", "spendgate: given twice: --pct\n"),
    row(["cost", "--by"], "lark-s 1 1\n", 2, "", "spendgate: missing value for --by\n"),
    row(["budget", "--limit", "1", "--warn"], "lark-s 1 1\n", 2, "", "spendgate: missing value for --warn\n"),
    row(["cost", "--by", "--by"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --by\n"),
    row(["cost", "--by", "Model"], "lark-s 1 1\n", 2, "", "spendgate: bad value for --by\n"),
    row(["budget", "--warn", "50"], "lark-s 1 1\n", 2, "", "spendgate: missing --limit\n"),
    row(["cost", "--by", "x"], "frob\n", 2, "", "spendgate: bad value for --by\n"),
    row(["frob", "--by"], "", 2, "", "spendgate: unknown command frob\n"),
    row(["help", "--by"], "", 0, "usage: spendgate check\n       spendgate models\n       spendgate cost [--by model|line]\n       spendgate fit [--pct N]\n       spendgate budget --limit USD [--warn N]\n", ""),
    row(["cost", "--by", "model"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "lark-s 1 record in 1000 out 200 cached 0 $0.000360\nlark-m 1 record in 5000 out 100 cached 2000 $0.005400\nwren-s 1 record in 30000 out 5000 cached 0 $0.005000\ntotal 3 records $0.010760\n", ""),
    row(["cost", "--by", "line"], "", 0, "total 0 records $0.000000\n", ""),
    row(["fit", "--pct", "1"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 1, "line 2 lark-m uses 5100 of 200000 tokens (2.6%)\nline 3 wren-s uses 35000 of 32000 tokens (109.4%)\nover 2 of 3 records\n", ""),
    row(["budget", "--warn", "50", "--limit", "0.02"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "spent $0.010760 of $0.020000 (53.8%)\nwarning: at or above 50% of the limit\n", ""),
    row(["budget", "--limit", "0.02", "--warn", "100"], "lark-s 1000 200\nlark-m 5000 100 2000\nwren-s 30000 5000\n", 0, "spent $0.010760 of $0.020000 (53.8%)\nwithin the limit\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
