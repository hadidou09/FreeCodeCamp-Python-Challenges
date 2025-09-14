** start of main.py **

def too_much_screen_time(hours):
    value = False
    days_avg = 0
    week_avg = 0
    for day in hours:
        if day >= 10:
            value = True
        else:
            continue
    for day in hours:
        week_avg += day
    week_avg = week_avg/7
    if week_avg >= 6:
        value = True
    for i in range(5):
        start = 0 + i
        end = 3 + i
        for day in range(start, end):
            days_avg += hours[day]
        days_avg = days_avg/3
        if days_avg >= 8:
            value = True
        else:
            days_avg = 0
            continue

    return value

** end of main.py **

