** start of main.py **

def speeding(speeds, limit):
    cars_speeding = 0
    speed_limit_values = list()
    results = list()
    for num in speeds:
        if num > limit:
            cars_speeding += 1
            speed = num - limit
            speed_limit_values.append(speed)


    average_speed = 0
    for num in speed_limit_values:
        average_speed += num
    if len(speed_limit_values) == 0:
        results = [0, 0]
    else:
        average_speed = average_speed/len(speed_limit_values)
        results.append(cars_speeding)
        results.append(average_speed)

    return results


** end of main.py **

