n = int(input())
num_list = [int(x) for x in input().split()]
result = 0
for x in num_list:
    if (x + 1) in num_list:
        result += 1
print(result, end='')