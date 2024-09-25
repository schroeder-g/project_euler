from collections import OrderedDict


days_in_month_map = OrderedDict(
    jan=31,
    feb=28,
    mar=31,
    apr=30,
    may=31,
    jun=30,
    july=31,
    aug=31,
    sep=30,
    oct=31,
    nov=30,
    dec=31,
)

weekday_map = {
    "mon": 0,
    "tues": 1,
    "wed": 2,
    "thurs": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}


def is_leap_year(y):
    return (y % 4 == 0 and not y % 100 == 0) or y % 400 == 0


def get_num_days_in_year(y):
    return 366 if is_leap_year(y) else 365


def is_first_day_of_month(num, y):
    for v in days_in_month_map.values():
        if num == 1:
            return True
        elif num < 1:
            return False

        num -= v
        if v == 28 and is_leap_year(y):
            num -= 1

    return False


def get_day_of_week(first_dow, num):
    day_num = (weekday_map[first_dow] + num - 1) % 7
    return [day for day in weekday_map if weekday_map[day] == day_num][0]


def get_sum_first_month_day_occurrences_in_year(first_dow, target_dow, y):
    total = 0
    for day in [
        1,
        32,
        60,
        61,
        91,
        92,
        121,
        122,
        152,
        153,
        182,
        183,
        213,
        214,
        244,
        245,
        274,
        275,
        305,
        306,
        335,
        336,
    ]:
        if (
            is_first_day_of_month(day, y)
            and get_day_of_week(first_dow, day) == target_dow
        ):
            total += 1

    return total


def get_total_first_sundays_from_1901_to_2000():
    first_weekdays = {}
    days_passed = 1
    sum_ = 0

    for year in range(1900, 2001):
        first_weekdays[year] = get_day_of_week("mon", days_passed)
        days_passed += get_num_days_in_year(year)

        if year > 1900:
            sum_ += get_sum_first_month_day_occurrences_in_year(
                first_weekdays[year], "sun", year
            )
    return sum_
