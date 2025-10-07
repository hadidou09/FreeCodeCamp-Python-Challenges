** start of main.py **

import re
def check_strength(password):
    status = ''
    conditions = 0

    if len(password) >= 8:
        conditions += 1
    if re.findall('[a-z]',password) and re.findall('[A-Z]',password):
        conditions += 1
    if re.findall('[0-9]',password):
        conditions += 1
    if re.findall('[@#$%^&*!]',password):
        conditions += 1
    
    if conditions < 2:
        status = 'weak'
    elif conditions == 2:
        status = 'medium'
    elif conditions == 3:
        status = 'medium'
    else:
        status = 'strong'
    
    
    return status
check_strength("pass!!!")

** end of main.py **

