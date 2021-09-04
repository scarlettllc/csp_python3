n = int(input())
counts = [0, 0, 0, 0]
i = 0
count = 0
while True:
    i += 1
    if i % 7 == 0 or '7' in str(i):
        if i % 4 == 1:
            counts[0] += 1
        elif i % 4 == 2:
            counts[1] += 1
        elif i % 4 == 3:
            counts[2] += 1
        else:
            counts[3] += 1
    else:
        count += 1
        if count == n:
            break
print(counts[0])
print(counts[1])
print(counts[2])
print(counts[3], end='')