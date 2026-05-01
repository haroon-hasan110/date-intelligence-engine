

from datetime import date


def parse_date(date_str):

    if not date_str or not date_str.strip():
        raise ValueError("enter the date again: Format: YYYY-MM-DD")

    date_str = date_str.strip()

    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError(f" wrong Format : '{date_str}' — try this format: YYYY-MM-DD")

    try:
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    except ValueError:
        raise ValueError("Year, month, and day in numbers Format: YYYY-MM-DD")

    if not (1 <= year <= 9999):
        raise ValueError(f"Year not valid i: {year} — 1  9999 ")

    try:
        date(year, month, day)
    except ValueError:
        raise ValueError(
            f"Invalid date: {day}/{month}/{year} — "
            f"Check month 1-12 day month is valid"
        )

    return year, month, day