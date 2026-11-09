"""The budget command: compare exact spend with a configured limit."""

from spendgate.pricing import amount_text, call_cost
from spendgate.registry import reply
from spendgate.windows import share_text


def run(options, records):
    """Report exact spend and apply the strict budget and inclusive warning gates."""
    total = sum(call_cost(record) for record in records)
    limit = options["limit"] * 1000
    out = f"spent {amount_text(total)} of {amount_text(limit)} ({share_text(total, limit)})\n"

    if total > limit:
        out += f"over by {amount_text(total - limit)}\n"
        return reply(1, out, "")
    if "warn" in options and 100 * total >= options["warn"] * limit:
        out += f"warning: at or above {options['warn']}% of the limit\n"
        return reply(0, out, "")
    out += "within the limit\n"
    return reply(0, out, "")
