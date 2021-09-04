n = int(input())
array = [int(x) for x in input().split()]
max = array[0]
min = array[0]
for i in range(n):
    if array[i] > max:
        max = array[i]
    if array[i] < min:
        min = array[i]
if n % 2 == 0:
    middle = (array[int(n/2)] + array[int(n/2)-1]) / 2
else:
    middle = array[int((n-1)/2)]
print(max, end=' ')
if int(middle) == middle:
    print(int(middle), end=' ')
else:
    print('%.1f' % middle, end=' ')
print(min, end='')