from hijri_converter import Gregorian

DESI_WEEKDAYS = {
    "Monday": "Peer",
    "Tuesday": "Mangal",
    "Wednesday": "Budh",
    "Thursday": "Jumerat",
    "Friday": "Jumma",
    "Saturday": "Hafta",
    "Sunday": "Itwaar",
}

def get_islamic_date(year: int, month: int, day: int, gregorian_weekday: str) -> dict:
    hijri = Gregorian(year, month, day).to_hijri()

    return {
        "year": hijri.year,
        "month": hijri.month,
        "month_name": hijri.month_name(),
        "day": hijri.day,
        "weekday": DESI_WEEKDAYS.get(gregorian_weekday, gregorian_weekday),
    }