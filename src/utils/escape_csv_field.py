"""
CSV field escaping utility for proper CSV formatting.
"""


def escape_csv_field(field):
    """
    Properly escape a field for CSV format following RFC 4180 standard.

    CSV standard rules:
    - Fields containing commas, quotes, or newlines must be enclosed in double quotes
    - Double quotes within a field must be escaped by doubling them
    - None/null values become empty strings

    Args:
        field: The field value to escape (can be any type)

    Returns:
        str: The properly escaped CSV field

    Examples:
        >>> escape_csv_field("simple text")
        'simple text'
        >>> escape_csv_field("text with, comma")
        '"text with, comma"'
        >>> escape_csv_field(None)
        ''
    """
    if field is None:
        return ""

    field_str = str(field)

    # Check if field needs quoting
    needs_quoting = any(char in field_str for char in [',', '"', '\n', '\r'])

    if needs_quoting or field_str.strip() != field_str:  # Also quote if has leading/trailing spaces
        # Escape any existing double quotes by doubling them
        field_str = field_str.replace('"', '""')
        # Enclose in double quotes
        return f'"{field_str}"'

    return field_str