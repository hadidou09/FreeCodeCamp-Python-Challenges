** start of main.py **

def second_largest(arr):
    largest = 0
    garbage = list()
    for num in arr:
        if num > largest:
            largest = num
        else:
            continue
    for num in arr:
        if num == largest:
            garbage.append(num)
        else:
            continue
    for num in garbage:
        arr.remove(num)
    
    largest = 0
    for num in arr:
        if num > largest:
            largest = num
        else:
            continue

    return largest

** end of main.py **

