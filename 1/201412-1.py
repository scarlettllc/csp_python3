n = int(input())
num_list = [int(x) for x in input().split()]
result_list = []
count_dict = {}
for x in num_list:
    if x not in count_dict.keys():
        count_dict[x] = 0
    count_dict[x] += 1
    result_list.append(count_dict[x])
for x in result_list:
    print(x, end=' ')