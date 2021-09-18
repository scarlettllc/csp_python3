n, l, t = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
pos = [a[i] for i in range(n)]
dir = [1 for i in range(n)]
for i in range(n):
    if pos[i] == 1 or pos[i] == 0:
        dir[i] = -dir[i]
for step in range(t):
    for i in range(n):
        pos[i] += dir[i]
        if pos[i] == l or pos[i] == 0:
            dir[i] = -dir[i]
    for i in range(n):
        for j in range(i + 1, n):
            if pos[i] == pos[j]:
                dir[i] = -dir[i]
                dir[j] = -dir[j]
for i in range(n):
    print(pos[i], end=' ')