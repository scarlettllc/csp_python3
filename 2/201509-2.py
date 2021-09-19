leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
not_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y = int(input())
d = int(input())
flag = False
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    flag = True
if flag:
    months = leap_year
else:
    months = not_leap_year
month = 1
day = 0
i = 0
while d - months[i] > 0:
    month += 1
    d -= months[i]
    i += 1
print(month)
print(d)