n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
result = []
for k in range(0, n):
    if k % 2 == 0:
        for i in range(k, -1, -1):
            result.append(matrix[i][k - i])
            i -= 1
    else:
        for i in range(0, k + 1, 1):
            result.append(matrix[i][k - i])
            i += 1
for k in range(n, 2 * n - 1):
    if k % 2 == 0:
        for i in range(n - 1, k - n, -1):
            result.append(matrix[i][k - i])
            i -= 1
    else:
        for i in range(k - n + 1, n):
            result.append(matrix[i][k - i])
            i += 1
for i in range(n * n):
    print(result[i], end=' ')