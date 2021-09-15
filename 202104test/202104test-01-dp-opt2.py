# final version
n = int(input())
partial = 0
total = 3
for i in range(2, n+1):
    partial = (total - partial) % 10000000000000000
    total = (total * 2 + partial) % 10000000000000000
result = str(total)
if n <= 36:
    print(result)
else:
    print('......', end='')
    print(result[-10:], end='')