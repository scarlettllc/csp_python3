n, m = [int(x) for x in input().split()]
windows = []
for i in range(n):
    windows.append([int(x) for x in input().split()])
points = []
for i in range(m):
    points.append([int(x) for x in input().split()])
seqs = [i for i in range(n)]
result = []
for i in range(m):
    flag = False
    for k in range(n - 1, -1, -1):
        if windows[seqs[k]][0] <= points[i][0] <= windows[seqs[k]][2] and windows[seqs[k]][1] <= points[i][1] <= windows[seqs[k]][3]:
            temp = seqs[k]
            seqs.remove(temp)
            seqs.append(temp)
            result.append(temp + 1)
            flag = True
            break
    if not flag:
        result.append("IGNORED")
for i in range(m):
    print(result[i])