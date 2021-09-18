n = int(input())
a = [int(x) for x in input().split()]
seats = [0 for x in range(100)]
result = []
for i in range(n):
    p = a[i]
    temp = []
    if p == 1:
        for j in range(100):
            if seats[j] == 0:
                seats[j] = 1
                temp.append(j + 1)
                break
        result.append(temp)
    elif p == 2:
        flag = True
        for j in range(0, 100, 5):
            if not flag:
                break
            for k in range(0, 4):
                if seats[j + k] == 0 and seats[j + k + 1] == 0:
                    seats[j + k] = 1
                    seats[j + k + 1] = 1
                    temp.append(j + k + 1)
                    temp.append(j + k + 2)
                    flag = False
                    break
        if flag:
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
        result.append(temp)
    elif p == 3:
        flag = True
        for j in range(0, 100, 5):
            if not flag:
                break
            for k in range(0, 3):
                if seats[j + k] == 0 and seats[j + k + 1] == 0 and seats[j + k + 2] == 0:
                    seats[j + k] = 1
                    seats[j + k + 1] = 1
                    seats[j + k + 2] = 1
                    temp.append(j + k + 1)
                    temp.append(j + k + 2)
                    temp.append(j + k + 3)
                    flag = False
                    break
        if flag:
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
        result.append(temp)
    elif p == 4:
        flag = True
        for j in range(0, 100, 5):
            if not flag:
                break
            for k in range(0, 2):
                if seats[j + k] == 0 and seats[j + k + 1] == 0 and seats[j + k + 2] == 0 and seats[j + k + 3] == 0:
                    seats[j + k] = 1
                    seats[j + k + 1] = 1
                    seats[j + k + 2] = 1
                    seats[j + k + 3] = 1
                    temp.append(j + k + 1)
                    temp.append(j + k + 2)
                    temp.append(j + k + 3)
                    temp.append(j + k + 4)
                    flag = False
                    break
        if flag:
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
        result.append(temp)
    elif p == 5:
        flag = True
        for j in range(0, 100, 5):
            if seats[j] == 0:
                seats[j] = 1
                seats[j + 1] = 1
                seats[j + 2] = 1
                seats[j + 3] = 1
                seats[j + 4] = 1
                temp.append(j + 1)
                temp.append(j + 2)
                temp.append(j + 3)
                temp.append(j + 4)
                temp.append(j + 5)
                flag = False
                break
        if flag:
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
            for j in range(0, 100):
                if seats[j] == 0:
                    seats[j] = 1
                    temp.append(j + 1)
        result.append(temp)
for i in range(n):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print('')