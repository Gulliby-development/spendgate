"""Exact integer pricing helpers for spendgate."""

from spendgate.registry import MODELS

_PRICES = {
    name: (input_price, output_price, cached_price)
    for name, input_price, output_price, cached_price, _ in MODELS
}


def call_cost(record):
    """Return the exact cost of a validated call in nano-dollars."""
    input_price, output_price, cached_price = _PRICES[record["model"]]
    uncached = record["input"] - record["cached"]
    return 10 * (
        uncached * input_price + record["cached"] * cached_price + record["output"] * output_price
    )


def amount_text(nanodollars):
    """Format nano-dollars as a six-decimal dollar amount, rounded half up."""
    microdollars = (nanodollars + 500) // 1000
    whole, fraction = divmod(microdollars, 1000000)
    return f"${whole}.{fraction:06d}"
