** start of main.py **

def classification(temp):
    classification = ''
    if temp >= 30000:
        classification = 'O'
    elif temp >= 10000 and temp <= 29999:
        classification = 'B'
    elif temp >= 7500 and temp <= 9999:
        classification = 'A'
    elif temp >= 6000 and temp <= 7499:
        classification = 'F'
    elif temp >= 5200 and temp <= 5999:
        classification = 'G'
    elif temp >= 3700 and temp <= 5199:
        classification = 'K'
    else:
        classification = 'M'

    return classification

** end of main.py **

