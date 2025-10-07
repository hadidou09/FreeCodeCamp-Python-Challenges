def has_exoplanet(readings):
    status = None
    readings_list = []
    average_luminosity = 0

    for char in readings:
        if char.isdigit():
            char = int(char)
            readings_list.append(char)
        else:
            order = ord(char.lower()) - ord('a') + 1
            readings_list.append(order)
    
    for num in readings_list:
        average_luminosity += num
    
    average_luminosity = (average_luminosity/len(readings_list))

    criteria = (average_luminosity * 80)/100

    for num in readings_list:
        if num <= criteria:
            status = True
            break
        else:
            status = False
            continue

    return status





