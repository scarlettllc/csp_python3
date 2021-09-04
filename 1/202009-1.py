n, X, Y = [int(x) for x in input().split()]
d = [0 for i in range(n)]
for i in range(n):
    x, y = [int(_) for _ in input().split()]
    d[i] = pow(X - x, 2) + pow(Y - y, 2)
index_list = [i[0] for i in sorted(enumerate(d), key=lambda x:x[1])]
print(index_list[0] + 1)
print(index_list[1] + 1)
print(index_list[2] + 1, end='')
