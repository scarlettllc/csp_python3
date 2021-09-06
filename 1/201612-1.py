n = int(input())
num_list = [int(x) for x in input().split()]
result = -1
for x in num_list:
    larger = 0
    smaller = 0
    for y in num_list:
        if y > x:
            larger += 1
        if y < x:
            smaller += 1
    if larger == smaller:
        result = x
print(result, end='')