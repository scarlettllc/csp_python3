n, L, r, t = [int(x) for x in input().split()]
A = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    A[i] = [int(x) for x in input().split()]
psum = [[0 for j in range(n + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + A[i - 1][j - 1]
result = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        top = max(1, i - r)
        bottom = min(n, i + r)
        left = max(1, j - r)
        right = min(n, j + r)
        sum = psum[bottom][right] - psum[bottom][left - 1] - psum[top - 1][right] + psum[top - 1][left - 1]
        if sum <= (right - left + 1) * (bottom - top + 1) * t:
            result += 1
print(result, end='')