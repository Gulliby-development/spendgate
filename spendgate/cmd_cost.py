"""The cost command: report exact usage costs by model or input line."""

from spendgate.pricing import amount_text, call_cost
from spendgate.registry import reply
from spendgate.report import plural


def run(options, records):
    """Return costs grouped by model or listed in input order, plus the exact total."""
    total_cost = 0
    lines = []

    if options["by"] == "line":
        for record in records:
            cost = call_cost(record)
            total_cost += cost
            lines.append(f"line {record['line']} {record['model']} {amount_text(cost)}\n")
    else:
        groups = {}
        for record in records:
            model = record["model"]
            cost = call_cost(record)
            total_cost += cost
            if model not in groups:
                groups[model] = {
                    "count": 0,
                    "input": 0,
                    "output": 0,
                    "cached": 0,
                    "cost": 0,
                }
            group = groups[model]
            group["count"] += 1
            group["input"] += record["input"]
            group["output"] += record["output"]
            group["cached"] += record["cached"]
            group["cost"] += cost

        for model, group in groups.items():
            lines.append(
                f"{model} {plural(group['count'], 'record')} in {group['input']} "
                f"out {group['output']} cached {group['cached']} "
                f"{amount_text(group['cost'])}\n"
            )

    lines.append(f"total {plural(len(records), 'record')} {amount_text(total_cost)}\n")
    return reply(0, "".join(lines), "")
