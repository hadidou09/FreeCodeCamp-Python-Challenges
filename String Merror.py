** start of main.py **

def is_mirror(str1, str2):
    value = None
    str1 = str1[-1::-1]
    for char in str2:
        if char.isdigit():
            continue
        elif char.isalpha():
            continue
        elif char == "!":
            str2 = str2.replace(char,"")
        else:
            str2 = str2.replace(char," ")
    str2 = str2.strip()
    print(str1)
    print(str2)
    if str1 == str2:
        value = True
    else:
        value = False
    return value

is_mirror("Hello World", "!dlroW !olleH")

** end of main.py **

