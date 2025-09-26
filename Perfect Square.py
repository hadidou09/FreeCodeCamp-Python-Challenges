** start of main.py **

import math
def is_perfect_square(n):
    status = None
    if n > 0:
        n = str(math.sqrt(n))
        print(n)
        for i in n[::-1]:
            if i == '0':
                n = n.replace(i,'')
            elif i == '.':
                n = n.replace(i,'')
            else:
                status = False
                break
    elif n == 0:
        status == True
        n = '0'
    else:
        status = False
        n = "not digit"

    for char in n:
        if char.isdigit():
            status = True
            continue
        else:
            status = False
            break

    return status

is_perfect_square(0)

** end of main.py **

