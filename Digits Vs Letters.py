** start of main.py **

def digits_or_letters(s):
    digits_count = 0
    letters_count = 0
    status = None
    for char in s:
        if char.isdigit():
            digits_count += 1
        elif char.isalpha():
            letters_count += 1
        else:
            continue
    if digits_count == letters_count:
        status = 'tie'
    elif digits_count > letters_count:
        status = 'digits'
    elif digits_count < letters_count:
        status = 'letters'
    return status
    

digits_or_letters("abc123")

** end of main.py **

