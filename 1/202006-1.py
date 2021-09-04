n, m = [int(x) for x in input().split()]
points = [['_' for j in range(3)] for i in range(n)]
points_A = []
points_B = []
for i in range(n):
    points[i] = input().split()
    points[i][0] = int(points[i][0])
    points[i][1] = int(points[i][1])
    if points[i][2] == 'A':
        points_A.append(i)
    else:
        points_B.append(i)
lines_yes_no = []
for i in range(m):
    flag = False
    theta_0, theta_1, theta_2 = [int(x) for x in input().split()]
    points_pos = []
    points_neg = []
    for k in range(n):
        temp = theta_0 + theta_1 * points[k][0] + theta_2 * points[k][1]
        if int(temp) == 0:
            break
        elif int(temp) > 0:
            points_pos.append(k)
        else:
            points_neg.append(k)
    if (points_pos == points_A and points_neg == points_B) or (points_pos == points_B and points_neg == points_A):
        flag = True
    else:
        flag = False
    if flag:
        lines_yes_no.append('Yes')
    else:
        lines_yes_no.append('No')
for i in range(m - 1):
    print(lines_yes_no[i])
print(lines_yes_no[m - 1], end='')