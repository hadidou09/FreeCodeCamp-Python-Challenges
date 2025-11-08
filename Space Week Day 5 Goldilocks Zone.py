** start of main.py **

import math
def goldilocks_zone(mass):
    luminosity = mass**3.5
    start = round(0.95 * math.sqrt(luminosity),2)
    end = round(1.37 * math.sqrt(luminosity),2)
    Goldilocks_zone = [start, end]
    return Goldilocks_zone


** end of main.py **

