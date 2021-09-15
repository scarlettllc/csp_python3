n = int(input())
dp = [[0 for j in range(7)] for i in range(n)]
dp[0][1] = 1
dp[0][2] = 1
dp[0][3] = 1
dp[1][4] = 1
dp[1][5] = 1
dp[1][6] = 1
dp[1][1] = 3
dp[1][2] = 3
dp[1][3] = 3
for i in range(2, n):
    dp[i][4] = dp[i-1][1] - dp[i-1][4]
    dp[i][5] = dp[i-1][2] - dp[i-1][5]
    dp[i][6] = dp[i-1][3] - dp[i-1][6]
    dp[i][1] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3] - dp[i-1][4]
    dp[i][2] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3] - dp[i-1][5]
    dp[i][3] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3] - dp[i-1][6]
result = dp[n-1][1] + dp[n-1][2] + dp[n-1][3]
result = str(result)
if len(result) <= 16:
    print(result)
else:
    print('......', end='')
    print(result[-10:], end='')