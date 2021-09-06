n, m = [int(x) for x in input().split()]
matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    matrix[i] = [int(x) for x in input().split()]
for j in range(m-1, -1, -1):
    for i in range(0, n):
        print(matrix[i][j], end=' ')
    print('')