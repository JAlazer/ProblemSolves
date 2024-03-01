# Counting Sundays
# 30 days- Sept. Apr. Jun. Nov.
# 31 days - Jan. Mar. May. Jul. Aug. Oct. Dec.
# Feb 28 day (29 days when year % 4 == 0)
import time


def is_leap(year):
    if (year % 400)%4 != 0:
        return False
    else:
        return True


