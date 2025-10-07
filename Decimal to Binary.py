** start of main.py **

import math
def to_binary(decimal):
    remainders = []
    result = ''
    while decimal > 0:   
        remaining = decimal % 2
        remainders.append(str(remaining))
        decimal = math.floor(decimal - (decimal/2))

    remainders = remainders[len(remainders)::-1]

    for num in remainders:
        result += num
    
    return result


** end of main.py **

