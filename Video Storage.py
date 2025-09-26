** start of main.py **

import math
def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    value = None

    if video_unit == 'KB':
        video_size = video_size/(1000**2)
    elif video_unit == 'MB':
        video_size = video_size/1000
    elif video_unit == 'GB':
        pass

    if drive_unit == 'GB':
        pass
    elif drive_unit == 'TB':
        drive_size = drive_size * 1000

    if video_unit != 'KB' and video_unit != 'MB' and video_unit != 'GB':
        value = "Invalid video unit"
    elif drive_unit != 'GB' and drive_unit != 'TB':
        value = "Invalid drive unit"
    else:
        value = math.floor(drive_size/video_size)
    print(value)
    return value
number_of_videos(2000, "B", 1, "TB")



** end of main.py **

