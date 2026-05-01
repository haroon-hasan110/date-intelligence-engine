from datetime import date

def get_gregorian_info(year: int, month: int, day: int) -> dict:
    d = date(year, month, day)
    return {
        "year": year,
        "month": month,
        "month_name": d.strftime("%B"),
        "day": day,
        "weekday": d.strftime("%A"),
    }