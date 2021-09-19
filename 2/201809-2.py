n = int(input())
h = [[]]
w = [[]]
for i in range(n):
    temp_list = [int(x) for x in input().split()]
    h.append(temp_list)
for i in range(n):
    temp_list = [int(x) for x in input().split()]
    w.append(temp_list)
dp = [0 for i in range(n+1)]
for j in range(1, n + 1):
    temp_result = 0
    for i in range(1, n + 1):
        if w[j][0] < h[i][1] and w[j][1] > h[i][0]:
            temp_result += min(h[i][1] - w[j][0], w[j][1] - h[i][0], w[j][1] - w[j][0], h[i][1] - h[i][0])
    dp[j] = dp[j - 1] + temp_result
print(dp[n])