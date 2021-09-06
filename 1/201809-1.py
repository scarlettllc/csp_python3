n = int(input())
num_list = [int(x) for x in input().split()]
result = [0 for i in range(n)]
result[0] = int((num_list[0] + num_list[1]) / 2)
result[n - 1] = int((num_list[n - 1] + num_list[n - 2]) / 2)
for i in range(1, n - 1):
    result[i] = int((num_list[i - 1] + num_list[i] + num_list[i + 1]) / 3)
for i in range(n):
    print(result[i], end=' ')