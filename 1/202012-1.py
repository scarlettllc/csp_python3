n = int(input())
weight_sum = 0
for i in range(n):
    w, score = [int(x) for x in input().split()]
    weight_sum += w * score
weight_sum = max(0, weight_sum)
print(weight_sum, end='')