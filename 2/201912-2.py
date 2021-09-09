n = int(input())
points = [[0 for j in range(2)] for i in range(n)]
for i in range(n):
    points[i] = [int(x) for x in input().split()]
result = [0 for i in range(5)]
for point in points:
    x = point[0]
    y = point[1]
    if [x, y + 1] in points and [x, y - 1] in points and [x + 1, y] in points and [x - 1, y] in points:
        temp_result = 0
        if [x + 1, y + 1] in points:
            temp_result += 1
        if [x + 1, y - 1] in points:
            temp_result += 1
        if [x - 1, y + 1] in points:
            temp_result += 1
        if [x - 1, y - 1] in points:
            temp_result += 1
        result[temp_result] += 1
for i in range(5):
    print(result[i])