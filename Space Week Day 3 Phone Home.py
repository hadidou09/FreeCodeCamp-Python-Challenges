** start of main.py **

def send_message(route):
    times = []
    results = 0

    last_route = route[len(route) - 1]     
    times.append(last_route/300000)
    route.remove(last_route)
    
    for num in route:
        num = (num/300000) + 0.5
        times.append(num)

    results = sum(times)
    results = round(results, 4)
    
    return results


** end of main.py **

