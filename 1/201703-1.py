n, k = [int(x) for x in input().split()]
num_list = [int(x) for x in input().split()]
result = 0
i = 0
while i < n:
    temp_sum = num_list[i]
    while temp_sum < k and i < n - 1:
        i += 1
        temp_sum += num_list[i]
    if temp_sum >= k or i == n - 1:
        result += 1
    i += 1
print(result, end='')