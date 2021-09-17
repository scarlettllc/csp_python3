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

def count_rps(idx_list, rps_result, last_result, flag, idx):
    result = last_result
    change = 0
    if flag == 'insert':
        for i in range(len(idx_list)):
            if a_isrp[i][idx]:
                change += 1
        result += change
        rps_result.append(result)
        idx_list.append(idx)
        return result
    else:
        idx_list.remove(idx)
        for i in range(len(idx_list)):
            if a_isrp[i][idx]:
                change += 1
        result -= change
        rps_result.append(result)
        return result

n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
query = []
for i in range(q):
    query.append(int(input()) - 1)
a_isrp = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i, n):
        if isrp(a[i], a[j]):
            a_isrp[i][j] = True
            a_isrp[j][i] = True

idx_list = []
rps_result = [0 for i in range(q)]
for i in range(q):
    if i == 0:
        last_result = 0
    else:
        last_result = rps_result[-1]
    if query[i] not in idx_list:
        print(count_rps(idx_list, rps_result, last_result, 'insert', query[i]))
    else:
        print(count_rps(idx_list, rps_result, last_result, 'delete', query[i]))