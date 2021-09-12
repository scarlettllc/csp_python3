n = int(input())
result_list = []
for i in range(n):
    expre = input()
    expre = expre.replace('x', '*').replace('/', '//')
    expre = eval(expre)
    if expre == 24:
        result_list.append('Yes')
    else:
        result_list.append('No')
for item in result_list:
    print(item)