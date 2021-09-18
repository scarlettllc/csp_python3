n = int(input())
a = [i + 1 for i in range(n)]
m = int(input())
for i in range(m):
    p, q = [int(x) for x in input().split()]
    for i in range(n):
        if a[i] == p:
            idx = i
            break
    if q > 0:
        for i in range(idx, idx + q):
            a[i] = a[i + 1]
        a[idx + q] = p
    else:
        for i in range(idx, idx + q, -1):
            a[i] = a[i - 1]
        a[idx + q] = p
for i in range(n):
    print(a[i], end=' ')