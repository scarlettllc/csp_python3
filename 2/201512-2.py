n, m = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
t = [[1 for j in range(m)] for i in range(n)]
for i in range(1, n - 1):
    for j in range(m):
        if (matrix[i - 1][j] == matrix[i][j] and matrix[i + 1][j] == matrix[i][j]):
            t[i][j] = 0
            k = i - 1
            while k >= 0:
                if matrix[k][j] == matrix[k + 1][j]:
                    t[k][j] = 0
                else:
                    break
                k -= 1
            k = i + 1 
            while k < n:
                if matrix[k][j] == matrix[k - 1][j]:
                    t[k][j] = 0
                else:
                    break
                k += 1
for j in range(1, m - 1):
    for i in range(n):
        if (matrix[i][j + 1] == matrix[i][j] and matrix[i][j - 1] == matrix[i][j]):
            t[i][j] = 0
            k = j - 1
            while k >= 0:
                if matrix[i][k] == matrix[i][k + 1]:
                    t[i][k] = 0
                else:
                    break
                k -= 1
            k = j + 1
            while k < m:
                if matrix[i][k] == matrix[i][k - 1]:
                    t[i][k] = 0
                else:
                    break
                k += 1
for i in range(n):
    for j in range(m):
        if t[i][j]:
            print(matrix[i][j], end=' ')
        else:
            print(0, end=' ')
    print('')