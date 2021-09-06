N = int(input())
num_list = [int(x) for x in input().split()]
pos_set = set()
for x in num_list:
    if x > 0:
        pos_set.add(x)
result = 0
for x in num_list:
    if x < 0:
        if -x in pos_set:
            result += 1
print(result, end='')