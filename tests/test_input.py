from harness import row, rows_test

# fmt: off
ROWS = [
    row(["check"], "", 0, "ok 0 records\n", ""),
    row(["check"], "  \t \n\t\n", 0, "ok 0 records\n", ""),
    row(["check"], "# note\n", 0, "ok 0 records\n", ""),
    row(["check"], "  # note\nlark-s 1 1\n", 0, "ok 1 record\n", ""),
    row(["check"], "lark-s 1 1", 0, "ok 1 record\n", ""),
    row(["check"], "lark-s 1 1\r\n", 0, "ok 1 record\n", ""),
    row(["check"], "lark-s 1 1\r\r\n", 1, "", "spendgate: line 1: bad output 1\r\n"),
    row(["check"], "lark-s\t1\t1\n", 0, "ok 1 record\n", ""),
    row(["check"], "  lark-s \t 1   1  \n", 0, "ok 1 record\n", ""),
    row(["check"], "lark-s 1\n", 1, "", "spendgate: line 1: expected MODEL INPUT OUTPUT [CACHED]\n"),
    row(["check"], "lark-s 1 2 3 4\n", 1, "", "spendgate: line 1: expected MODEL INPUT OUTPUT [CACHED]\n"),
    row(["check"], "Lark-s 1 1\n", 1, "", "spendgate: line 1: unknown model Lark-s\n"),
    row(["check"], "lark-xl 1 1\n", 1, "", "spendgate: line 1: unknown model lark-xl\n"),
    row(["check"], "lark-s x 1\n", 1, "", "spendgate: line 1: bad input x\n"),
    row(["check"], "lark-s 01 1\n", 1, "", "spendgate: line 1: bad input 01\n"),
    row(["check"], "lark-s 1 1000000001\n", 1, "", "spendgate: line 1: bad output 1000000001\n"),
    row(["check"], "lark-s 1 1 x\n", 1, "", "spendgate: line 1: bad cached x\n"),
    row(["check"], "lark-s 5 1 6\n", 1, "", "spendgate: line 1: cached exceeds input\n"),
    row(["check"], "frob x y\n", 1, "", "spendgate: line 1: unknown model frob\n"),
    row(["check"], "lark-s x y\n", 1, "", "spendgate: line 1: bad input x\n"),
    row(["check"], "lark-s 1 y 5\n", 1, "", "spendgate: line 1: bad output y\n"),
    row(["check"], "lark-s 5 1 x\n", 1, "", "spendgate: line 1: bad cached x\n"),
    row(["check"], "# c\n\nlark-s 1 1\nlark-s x 1\n", 1, "", "spendgate: line 4: bad input x\n"),
    row(["check"], "lark-s 1 1\nfrob 1 1\nlark-s x 1\n", 1, "", "spendgate: line 2: unknown model frob\n"),
    row(["check"], "lark-s \u0661 1\n", 1, "", "spendgate: line 1: bad input \u0661\n"),
    row(["check"], "lark-s\u00a01 1\n", 1, "", "spendgate: line 1: expected MODEL INPUT OUTPUT [CACHED]\n"),
    row(["cost"], "lark-s 1 1\nlark-s 1\n", 1, "", "spendgate: line 2: expected MODEL INPUT OUTPUT [CACHED]\n"),
    row(["budget", "--limit", "1"], "lark-s 1 x\n", 1, "", "spendgate: line 1: bad output x\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
