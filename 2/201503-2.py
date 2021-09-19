n = int(input())
a = [int(x) for x in input().split()]
count_dict = {}
for i in range(n):
    if a[i] not in count_dict.keys():
        count_dict[a[i]] = 0
    count_dict[a[i]] += 1
count_dict = sorted(count_dict.items(), key = lambda x: (x[1], -x[0]), reverse=True)
for item in count_dict:
    print('{} {}'.format(item[0], item[1]))