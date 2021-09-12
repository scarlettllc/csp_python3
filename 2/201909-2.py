n = int(input())
num_list = [0 for i in range(n)]
T = 0
D = 0
E = 0
for i in range(n):
    temp_list = [int(x) for x in input().split()]
    count = 0
    for j in range(1, len(temp_list)):
        if temp_list[j] > 0:
            if count != 0 and temp_list[j] != count:
                num_list[i] = 1
            count = temp_list[j]
        else:
            count += temp_list[j]
    T += count
for i in range(n):
    if num_list[i] == 1:
        D += 1
if n >= 3:
    for i in range(1, n - 1):
        if num_list[i] == 1 and num_list[i - 1] == 1 and num_list[i + 1] == 1:
            E += 1
    if n > 3:
        if num_list[0] == 1 and num_list[1] == 1 and num_list[n - 1] == 1:
            E += 1
        if num_list[n - 1] == 1 and num_list[n - 2] == 1 and num_list[0] == 1:
            E += 1
print("{} {} {}".format(T, D, E))

"""
# 正确题解
n = int(input())
num_list = [0 for i in range(n)]
T = 0
D = 0
E = 0
for i in range(n):
    temp_list = [int(x) for x in input().split()]
    count = 0
    for j in range(1, len(temp_list)):
        if temp_list[j] > 0:
            if count != 0 and temp_list[j] != count:
                num_list[i] = 1
            count = temp_list[j]
        else:
            count += temp_list[j]
    T += count
for i in range(n):
    if num_list[i] == 1:
        D += 1
if n >= 3:
    for i in range(1, n - 1):
        if num_list[i] == 1 and num_list[i - 1] == 1 and num_list[i + 1] == 1:
            E += 1
    if num_list[0] == 1 and num_list[1] == 1 and num_list[n - 1] == 1:
        E += 1
    if num_list[n - 1] == 1 and num_list[n - 2] == 1 and num_list[0] == 1:
        E += 1
print("{} {} {}".format(T, D, E))
"""