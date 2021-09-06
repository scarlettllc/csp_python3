n = int(input())
count_7 = n // 50
count_4 = (n - int(count_7 * 50)) // 30
count_1 = (n - int(count_7 * 50) - int(count_4 * 30)) // 10
result = int(count_7 * 7 + count_4 * 4 + count_1)
print(result, end='')
