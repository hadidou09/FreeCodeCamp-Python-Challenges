** start of main.py **

def all_unique(s):
    letters = list()
    for i in s:
        letters.append(i)
    list_length = len(letters)
    count = 0
    for i in range(list_length):
        the_letter = letters[i]
        for j in s:
            if j == the_letter:
                count += 1
                continue
            else:
                continue

    if count <= len(letters):
        return True
    else:
        return False
   




** end of main.py **

