n, k = [int(x) for x in input().split()]
a = [i + 1 for i in range(n)]
temp = 0
while len(a) > 1:
    b = [a[i] for i in range(len(a))]
    for i in range(len(b)):
        temp += 1
        if (temp % k == 0 or temp % 10 == k) and len(a) > 1:
            a.remove(b[i])
print(a[0], end='')