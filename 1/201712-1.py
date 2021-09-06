n = int(input())
num_list = [int(x) for x in input().split()]
num_list.sort()
result = 10000
for i in range(1, n):
    temp_result = abs(num_list[i] - num_list[i - 1])
    result = min(result, temp_result)
print(result, end='')
