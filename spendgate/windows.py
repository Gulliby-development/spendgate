"""Exact integer share formatting for spendgate."""


def share_text(numerator, denominator):
    """Format a nonnegative ratio as a percentage with one decimal, rounded half up."""
    tenths = (2000 * numerator + denominator) // (2 * denominator)
    whole, fraction = divmod(tenths, 10)
    return f"{whole}.{fraction}%"
