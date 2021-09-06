num_list = [int(x) for x in input().split()]
n = len(num_list)
score_list = [0 for i in range(n)]
result = 0
for i in range(n - 1):
    if num_list[i] == 1:
        score_list[i] = 1
        result += 1
    else:
        if i == 0 or (i > 0 and score_list[i - 1] == 1):
            score_list[i] = 2
            result += 2
        else:
            score_list[i] = score_list[i - 1] + 2
            result += score_list[i]
print(result, end='')