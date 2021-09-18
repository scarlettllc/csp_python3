n, k = [int(x) for x in input().split()]
time = {}
pos = [i + 1 for i in range(n)]
for i in range(k):
    w, s, c = [int(x) for x in input().split()]
    if s not in time:
        time[s] = []
    time[s].append({"id": w, "type": "borrow"})
    if (s + c) not in time:
        time[s + c] = []
    time[s + c].append({"id": w, "type": "return"})
time = sorted(time.items(), key = lambda x: x[0])
for t in time:
    t = list(t)
    t[1] = sorted(t[1], key = lambda x: (x["type"], -x["id"]), reverse=True)
    for op in t[1]:
        if op["type"] == 'return':
            for i in range(len(pos)):
                if pos[i] == 'X':
                    pos[i] = op["id"]
                    break
        else:
            for i in range(len(pos)):
                if pos[i] == op["id"]:
                    pos[i] = 'X'
                    break
for i in range(len(pos)):
    print(pos[i], end=' ')