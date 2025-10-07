** start of main.py **

def format_number(number):
    numbers_list = []
    final_number = ''

    numbers_list.append(number[0])
    numbers_list.append(number[1:4])
    numbers_list.append(number[4:7])
    numbers_list.append(number[7:])

    numbers_list[0] = '+'+ numbers_list[0]
    numbers_list[1] =' '+'('+ numbers_list[1]+')'+' '
    numbers_list[2] = numbers_list[2]+'-'

    final_number = numbers_list[0]+numbers_list[1]+numbers_list[2]+numbers_list[3]

    return final_number


** end of main.py **

