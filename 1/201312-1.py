n = int(input())
num_list = [int(x) for x in input().split()]
count_dict = {}
for x in num_list:
    if x not in count_dict.keys():
        count_dict[x] = 0
    count_dict[x] += 1
count_list = sorted(count_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)
print(count_list[0][0], end='')