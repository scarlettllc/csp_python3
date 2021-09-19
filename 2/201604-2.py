grid = []
for i in range(15):
    grid.append([int(x) for x in input().split()])
square = []
for i in range(4):
    square.append([int(x) for x in input().split()])
left = int(input())
left -= 1
grid_top = []
for j in range(left, left + 4):
    flag = True
    for i in range(15):
        if grid[i][j] == 1:
            grid_top.append(i)
            flag = False
            break
    if flag:
        grid_top.append(15)
square_bottom = []
for j in range(4):
    flag = True
    for i in range(3, -1, -1):
        if square[i][j] == 1:
            square_bottom.append(i)
            flag = False
            break
    if flag:
        square_bottom.append(-1)
j_0 = 0
least = grid_top[0] - square_bottom[0]
for j in range(1, 4):
    if grid_top[j] - square_bottom[j] < least:
        least = grid_top[j] - square_bottom[j]
        j_0 = j
for i in range(4):
    for j in range(4):
        if square[i][j] == 1:
            grid[i - square_bottom[j_0] + grid_top[j_0] - 1][j + left] = 1
for i in range(15):
    for j in range(10):
        print(grid[i][j], end=' ')
    print('')