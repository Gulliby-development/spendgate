"""Basic text formatting helpers shared by spendgate commands."""


def plural(count, noun):
    """Return a count with its singular noun only when count is one."""
    suffix = "" if count == 1 else "s"
    return f"{count} {noun}{suffix}"


def price_text(hundredths):
    """Format hundredths of a dollar as a two-decimal amount without a symbol."""
    whole, fraction = divmod(hundredths, 100)
    return f"{whole}.{fraction:02d}"
