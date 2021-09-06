n = int(input())
num_list = [int(x) for x in input().split()]
result = 0
for i in range(1, n):
    temp_result = abs(num_list[i] - num_list[i - 1])
    result = max(result, temp_result)
print(result, end='')