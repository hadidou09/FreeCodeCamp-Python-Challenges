** start of main.py **

def to_decimal(binary):
    position = 0
    decimal = 0
    binary = binary[::-1]

    for num in binary:
        decimal += int(num) * (2**position)
        position += 1

    return decimal
to_decimal("101")

** end of main.py **

