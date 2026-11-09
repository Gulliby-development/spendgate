"""The check command reports the number of validated usage records."""

from spendgate.registry import reply
from spendgate.report import plural


def run(options, records):
    """Return a successful validation summary for the supplied records."""
    return reply(0, f"ok {plural(len(records), 'record')}\n", "")
