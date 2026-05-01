SHAKA_MONTHS = [
    ("Chaitra", (3, 22), (4, 20)),
    ("Vaisakha", (4, 21), (5, 21)),
    ("Jyaistha", (5, 22), (6, 21)),
    ("Asadha", (6, 22), (7, 22)),
    ("Shravana", (7, 23), (8, 22)),
    ("Bhadra", (8, 23), (9, 22)),
    ("Asvina", (9, 23), (10, 22)),
    ("Kartika", (10, 23), (11, 21)),
    ("Agrahayana", (11, 22), (12, 21)),
    ("Pausa", (12, 22), (1, 20)),
    ("Magha", (1, 21), (2, 19)),
    ("Phalguna", (2, 20), (3, 21)),
]

def get_hindu_date(year: int, month: int, day: int, weekday: str) -> dict:
    if (month < 3) or (month == 3 and day < 22):
        shaka_year = year - 79
    else:
        shaka_year = year - 78

    shaka_month = None
    for name, start, end in SHAKA_MONTHS:
        sm, sd = start
        em, ed = end

        if sm <= em:
            if (month == sm and day >= sd) or (month == em and day <= ed) or (sm < month < em):
                shaka_month = name
        else:
            if (month == sm and day >= sd) or (month == em and day <= ed) or (month > sm or month < em):
                shaka_month = name

    return {
        "year": shaka_year,
        "month_name": shaka_month,
        "day": day,
        "weekday": weekday,
    }