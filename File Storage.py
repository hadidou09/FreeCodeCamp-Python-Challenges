** start of main.py **

import math
def number_of_files(file_size, file_unit, drive_size_gb):
    if file_unit == 'B':
        file_size = file_size/(1000*1000*1000)
    elif file_unit == 'KB':
        file_size = file_size/(1000*1000)
    elif file_unit == 'MB':
        file_size = file_size/1000
    number_of_files = drive_size_gb/file_size
    return math.floor(number_of_files)

** end of main.py **

