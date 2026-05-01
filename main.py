import textwrap
from validators import parse_date
from calendar_utils import get_gregorian_info
from islamic import get_islamic_date
from hindu import get_hindu_date
from zodiac import get_zodiac
from history import get_history


def build_date_profile(year, month, day):
    g = get_gregorian_info(year, month, day)
    weekday = g["weekday"]

    return {
        "calendar": {
            "gregorian": g,
            "islamic": get_islamic_date(year, month, day, weekday),
            "hindu": get_hindu_date(year, month, day, weekday),
        },
        "personality": {
            "zodiac": get_zodiac(month, day),
        },
        "history": get_history(month, day),
    }


def print_profile(profile):
    W = 52
    HR = "─" * W

    g = profile["calendar"]["gregorian"]
    isl = profile["calendar"]["islamic"]
    hin = profile["calendar"]["hindu"]
    z = profile["personality"]["zodiac"]

    def row(label, value):
        print(f"  {label:<13} {value}")

    print()
    print("┌" + "─" * W + "┐")
    print("│" + "DATE INTELLIGENCE ENGINE".center(W) + "│")
    print("└" + "─" * W + "┘\n")

    print(f"  {g['day']} {g['month_name']} {g['year']} · {g['weekday']}\n")

    print("  CALENDAR")
    print(f"  {HR}")
    row("Gregorian", f"{g['year']} · {g['month_name']} · {g['day']} · {g['weekday']}")
    row("Islamic", f"{isl['year']} · {isl['month_name']} · {isl['day']} · {isl['weekday']}")
    row("Hindu", f"{hin['year']} · {hin['month_name']} · {hin['day']} · {hin['weekday']}\n")

    print("  PERSONALITY")
    print(f"  {HR}")
    row("Zodiac", f"{z['name']} {z['symbol']} · {z['element']}")
    row("Traits", " · ".join(z["traits"]) + "\n")

    print("  ON THIS DAY")
    print(f"  {HR}")
    for line in textwrap.wrap(profile["history"], width=W - 2):
        print(f"  {line}")

    print(f"\n  {HR}\n")


def main():
    raw = input("Enter date (YYYY-MM-DD): ").strip()
    year, month, day = parse_date(raw)
    profile = build_date_profile(year, month, day)
    print_profile(profile)


if __name__ == "__main__":
    main()