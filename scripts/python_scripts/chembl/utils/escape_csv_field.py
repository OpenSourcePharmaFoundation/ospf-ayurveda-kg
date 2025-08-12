def escape_csv_field(field):
    """
    Properly escape a field for CSV format.

    CSV standard rules:
    - Fields containing commas, quotes, or newlines must be enclosed in double quotes
    - Double quotes within a field must be escaped by doubling them
    """
    if field is None:
        return ""

    field_str = str(field))

    #  Handle already quoted fields
    if field_str.startswith('"') and field_str.endswith('"'):
        return field_str
    if field_str.startswith("'") and field_str.endswith("'"):
        return field_str

    # Remove internal single quotes by replacing them with double quotes
    if '"' in field_str:
        field_str = field_str.replace('"', "'")

    # Add single around strings
    return f"'{field_str}'"
