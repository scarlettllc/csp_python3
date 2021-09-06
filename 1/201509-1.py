n = int(input())
num_list = [int(x) for x in input().split()]
result = 1
for i in range(1, n):
    if num_list[i] != num_list[i - 1]:
        result += 1
print(result, end='')