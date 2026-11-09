from harness import reads_rows, row

# fmt: off
ROWS = [
    row([], "", 0, "", ""),
    row(["help"], "", 0, "", ""),
    row(["-h"], "", 0, "", ""),
    row(["frob"], "", 0, "", ""),
    row(["models"], "", 0, "", ""),
    row(["check"], "", 1, "", ""),
    row(["cost"], "", 1, "", ""),
    row(["fit"], "", 1, "", ""),
    row(["budget", "--limit", "1"], "", 1, "", ""),
    row(["budget"], "", 0, "", ""),
    row(["cost", "--by", "x"], "", 0, "", ""),
    row(["fit", "--pct", "5", "--pct", "6"], "", 0, "", ""),
    row(["check", "extra"], "", 0, "", ""),
    row(["budget", "--warn", "5", "--limit", "1"], "", 1, "", ""),
]
# fmt: on

test_rows = reads_rows(ROWS)
