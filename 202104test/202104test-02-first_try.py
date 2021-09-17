def isrp(a, b):
    if a == 1 or b == 1:
        return True
    while True:
        t = a % b
        if t == 0:
            break
        else:
            a = b
            b = t
    if b > 1:
        return False
    else:
        return True

def count_rps(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if isrp(nums[i], nums[j]):
                result += 1
    return result

n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
query = []
for i in range(q):
    query.append(int(input()) - 1)
idx_set = set()
nums = []
for i in range(q):
    if query[i] not in idx_set:
        idx_set.add(query[i])
        nums.append(a[query[i]])
        print(count_rps(nums))
    else:
        idx_set.remove(query[i])
        nums.remove(a[query[i]])
        print(count_rps(nums))