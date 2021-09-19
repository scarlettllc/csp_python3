n = int(input())
points = []
x_max = 0
y_max = 0
for i in range(n):
    points.append([int(x) for x in input().split()])
    x_max = points[-1][2] if points[-1][2] > x_max else x_max
    y_max = points[-1][3] if points[-1][3] > y_max else y_max
matrix = [[0 for j in range(x_max)] for i in range(y_max)]
result = 0
for k in range(n):
    for i in range(points[k][1], points[k][3]):
        for j in range(points[k][0], points[k][2]):
            if not matrix[i][j]:
                matrix[i][j] = 1
                result += 1
print(result)