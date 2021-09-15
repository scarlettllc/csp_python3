global result
def dfs(temp_str, n, idx):
    if idx == n:
        global result
        result += 1
        return
    else:
        if idx >= 2:
            if temp_str[-2] == '1' and temp_str[-1] == '1':
                dfs(temp_str + '2', n, idx+1)
                dfs(temp_str + '3', n, idx+1)
            elif temp_str[-2] == '2' and temp_str[-1] == '2':
                dfs(temp_str + '1', n, idx+1)
                dfs(temp_str + '3', n, idx+1)
            elif temp_str[-2] == '3' and temp_str[-1] == '3':
                dfs(temp_str + '1', n, idx+1)
                dfs(temp_str + '2', n, idx+1)
            else:
                dfs(temp_str + '1', n, idx+1)
                dfs(temp_str + '2', n, idx+1)
                dfs(temp_str + '3', n, idx+1)
        else:
            dfs(temp_str + '1', n, idx+1)
            dfs(temp_str + '2', n, idx+1)
            dfs(temp_str + '3', n, idx+1)
result = 0
n = int(input())
dfs('', n, 0)
result = str(result)
if len(result) <= 16:
    print(result, end='')
else:
    print('......', end = '')
    print(result[-10:], end = '')