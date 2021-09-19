n = int(input())
points = []
x_max = 0
y_max = 0
for i in range(n):
    points.append([int(x) for x in input().split()])
    x_max = points[-1][2] if points[-1][2] > x_max else x_max
    y_max = points[-1][3] if points[-1][3] > y_max else y_max
result = 0
if n > 0:
    x_min = points[0][0]
    y_min = points[0][1]
    for i in range(1, n):
        x_min = points[i][0] if points[i][0] < x_min else x_min
        y_min = points[i][1] if points[i][1] < y_min else y_min
    matrix = [[0 for j in range(x_max - x_min)] for i in range(y_max - y_min)]
    for k in range(n):
        for i in range(points[k][1], points[k][3]):
            for j in range(points[k][0], points[k][2]):
                if not matrix[i - y_min][j - x_min]:
                    matrix[i - y_min][j - x_min] = 1
                    result += 1
print(result)