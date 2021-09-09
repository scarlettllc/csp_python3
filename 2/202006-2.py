n, a, b = [int(x) for x in input().split()]
dict_a = {}
for i in range(a):
    index, value = [int(x) for x in input().split()]
    dict_a[index] = value
dict_b = {}
for i in range(b):
    index, value = [int(x) for x in input().split()]
    dict_b[index] = value
common_keys = set(dict_a.keys()).intersection(dict_b.keys())
result = 0
for key in common_keys:
    result += dict_a[key] * dict_b[key]
print(result, end='')