t = int(input())
a = [0, 3500, 3500 + 1500, 3500 + 4500, 3500 + 9000, 3500 + 35000, 3500 + 55000, 3500 + 80000]
tax = [0, 0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
income = [0, 3500]
for i in range(2, len(a)):
    income.append(income[i - 1] + (a[i] - a[i - 1]) * (1 - tax[i - 1]))
i = 0
while i < len(income):
    if t <= income[i]:
        break
    i += 1
result = a[i - 1] + (t - income[i - 1]) / (1 - tax[i-1])
print(int(result))