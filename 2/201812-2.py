r, y, g = [int(x) for x in input().split()]
n = int(input())
result = 0
for i in range(n):
    k, t = [int(x) for x in input().split()]
    if k == 0:
        result += t
    elif k == 1:
        temp = result % (r + y + g)
        if 0 <= temp < t:
            result += (t - temp)
        elif t <= temp < (t + g):
            pass
        elif (t + g) <= temp < (t + g + y + r):
            result += (r + g + y + t - temp)
    elif k == 2:
        temp = result % (r + y + g)
        if 0 <= temp < (t + r):
            result += (t + r - temp)
        elif (t + r) <= temp < (t + r + g):
            pass
        elif (t + r + g) <= temp < (t + r  + g + r + y):
            result += (t + 2 * r + y + g - temp)
    else:
        temp = result % (r + y + g)
        if 0 <= temp < t:
            pass
        elif t <= temp < (t + y + r):
            result += (t + y + r - temp)
        elif (t + y + r) <= temp < (t + y + r + g):
            pass
print(result, end='')
