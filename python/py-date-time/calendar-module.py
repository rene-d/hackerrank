# Python > Date and Time > Calendar Module
# Print the day of a given date.
#
# https://www.hackerrank.com/challenges/calendar-module/problem
#

import calendar

m, d, y = map(int, input().split())

i = calendar.weekday(y, m, d)
print(calendar.day_name[i].upper())
