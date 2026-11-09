"""The fit command: report calls that exceed their model context threshold."""

from spendgate.registry import MODELS, reply
from spendgate.report import plural
from spendgate.windows import share_text


def run(options, records):
    """Return the records whose input and output exceed the selected context share."""
    windows = {model: window for model, _input, _output, _cached, window in MODELS}
    pct = options["pct"]
    lines = []

    for record in records:
        total = record["input"] + record["output"]
        window = windows[record["model"]]
        if 100 * total > pct * window:
            lines.append(
                f"line {record['line']} {record['model']} uses {total} of {window} tokens "
                f"({share_text(total, window)})\n"
            )

    count = len(lines)
    lines.append(f"over {count} of {plural(len(records), 'record')}\n")
    return reply(1 if count else 0, "".join(lines), "")
