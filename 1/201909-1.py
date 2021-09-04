N, M = [int(x) for x in input().split()]
sum = 0
max_idx = 0
remove = 1
for i in range(N):
    temp_list = [int(x) for x in input().split()]
    temp_remove = 0
    for j in range(1, M + 1):
        temp_remove += temp_list[j]
    sum += temp_list[0] + temp_remove
    if temp_remove < remove:
        max_idx = i
        remove = temp_remove
max_idx += 1
if remove < 0:
    remove = -remove
print('{} {} {}'.format(sum, max_idx, remove), end='')
