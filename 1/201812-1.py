r, y, g = [int(x) for x in input().split()]
result = 0
n = int(input())
for i in range(n):
    k, t = [int(x) for x in input().split()]
    if k == 0:
        result += t
    elif k == 1:
        result += t
    elif k == 2:
        result += r + t
print(result, end='')