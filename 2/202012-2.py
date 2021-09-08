n = int(input())
y_result = [[0 for j in range(2)] for j in range(n + 1)]
for i in range(1, n + 1):
    y_result[i] = [int(x) for x in input().split()]
y_result = sorted(y_result, key=lambda x: x[0])
prefix = [0 for i in range(n + 2)]
suffix = [0 for i in range(n + 2)]
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + (1 if y_result[i][1] == 0 else 0)
for i in range(n, 0, -1):
    suffix[i] = suffix[i + 1] + (1 if y_result[i][1] == 1 else 0)
p = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    if y_result[i][0] == y_result[i - 1][0]:
        p[i] = p[i - 1]
    else:
        p[i] = i
result = 0
max_count = 0
theta = 0
for i in range(1, n + 1):
    temp = prefix[p[i] - 1] + suffix[i]
    if temp >= max_count:
        max_count = temp
        theta = max(y_result[i][0], theta)
print(theta, end='')


'''
y = []
result = []
for i in range(n):
    y_i, result_i = [int(x) for x in input().split()]
    y.append(y_i)
    result.append(result_i)
counts = []
for theta in y:
    temp_count = 0
    for y_i, result_i in zip(y, result):
        if y_i >= theta:
            temp_result = 1
        else:
            temp_result = 0
        if temp_result == result_i:
            temp_count += 1
    counts.append(temp_count)
max_count = 0
for count in counts:
    if count > max_count:
        max_count = count
max_theta = 0
for idx, y_i in enumerate(y):
    if counts[idx] == max_count and y_i > max_theta:
        max_theta = y_i
print(max_theta, end='')
'''