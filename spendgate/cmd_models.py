"""The models command: print the built-in model price and context table."""

from spendgate.registry import MODELS, reply
from spendgate.report import price_text


def run(options, records):
    """Return the model table in registry order; this command ignores its input."""
    lines = [
        f"{name} in {price_text(input_price)} out {price_text(output_price)} "
        f"cached {price_text(cached_price)} context {window}\n"
        for name, input_price, output_price, cached_price, window in MODELS
    ]
    return reply(0, "".join(lines), "")
