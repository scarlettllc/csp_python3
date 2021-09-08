n, k, t, x_l, y_d, x_r, y_u = [int(x) for x in input().split()]
danger_points = [[0 for j in range(t)] for i in range(n)]
for i in range(n):
    temp_list = [int(x) for x in input().split()]
    for j in range(t):
        if x_l <= temp_list[2 * j] <= x_r and \
                y_d <= temp_list[2 * j + 1] <= y_u:
            danger_points[i][j] = 1
max_danger_counts = [0 for i in range(n)]
for i in range(n):
    p = [0 for j in range(t)]
    p[0] = danger_points[i][0]
    max_danger_counts[i] = max(max_danger_counts[i], p[0])
    for j in range(1, t):
        if danger_points[i][j] == 1:
            p[j] = p[j - 1] + 1
        else:
            p[j] = 0
        max_danger_counts[i] = max(max_danger_counts[i], p[j])
result_1 = 0
result_2 = 0
for count in max_danger_counts:
    if count != 0:
        result_1 += 1
    if count >= k:
        result_2 += 1
print(result_1)
print(result_2, end='')