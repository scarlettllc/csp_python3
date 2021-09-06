n = int(input())
num_list = [int(x) for x in input().split()]
result = 0
for i in range(n):
    if i > 0 and i < n - 1:
        if (num_list[i - 1] > num_list[i] and num_list[i + 1] > num_list[i]) \
                or (num_list[i - 1] < num_list[i] and num_list[i + 1] < num_list[i]):
            result += 1
print(result, end="")
