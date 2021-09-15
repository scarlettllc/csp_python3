def solution(n: int):
    pre = [[1, 0]] * 3
    for i in range(n-1):
        current = [[0, 0]] * 3
        total = sum(map(sum, pre))
        for k in range(3):
            current[k][0] = total - pre[k][1] - pre[k][0]
            current[k][1] = pre[k][0]
        pre = current
    total = str(sum(map(sum, pre)))
    if len(total) < 16:
        print(total)
    else:
        print("......", total[-10:], sep="")


if __name__ == "__main__":
    n = eval(input())
    solution(n)