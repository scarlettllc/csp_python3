n, m, L = [int(x) for x in input().split()]
h = [0 for x in range(0, L)]
for i in range(n):
    current_line = [int(x) for x in input().split()]
    for j in range(m):
        h[int(current_line[j])] += 1
for x in range(L-1):
    print(str(h[x]), end=' ')
print(h[L-1], end='')
