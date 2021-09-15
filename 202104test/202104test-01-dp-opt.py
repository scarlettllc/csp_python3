n = int(input())
dp = [[0 for j in range(2)] for i in range(n+1)]
dp[1][0] = 3
dp[2][0] = 9
dp[2][1] = 3
for i in range(3, n+1):
    dp[i][1] = (dp[i-1][0] - dp[i-1][1]) % 10000000000000000
    dp[i][0] = (dp[i-1][0] * 3 - dp[i-1][1]) % 10000000000000000
result = dp[n][0]
result = str(result)
if n <= 36:
    print(result)
else:
    print('......', end='')
    print(result[-10:], end='')