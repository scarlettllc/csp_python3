isbn = input()
num_str = isbn[0] + isbn[2:5] + isbn[6:11]
total = 0
for i in range(9):
    total += (i + 1) * int(num_str[i])
remainder = total % 11
if remainder == 10:
    code = 'X'
else:
    code = remainder
if isbn[-1] == str(code):
    print("Right")
else:
    print(isbn[:-1] + str(code))