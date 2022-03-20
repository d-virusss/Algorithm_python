from collections import deque


nextPos = {0: [1, 5, 6], 1: [0, 6, 2], 2: [1, 6, 3], 3: [2, 6, 4], 4: [3, 5, 6, ], 5: [0, 6, 4], 6: [0, 1, 2, 3, 4, 5]}
visited = {}

a = [1, 2, 3, 0, 6, 5, 4]
cnt = 0
visited[str(a)] = True
b = [1, 2, 3, 4, 5, 6, 0]

q = deque([[a, a.index(0), cnt]])


while(q):
    nextInfo = q.popleft()
    nextS1 = nextInfo[0]
    zero = nextInfo[1]
    count = nextInfo[2]

    visited[str(nextS1)] = True

    if nextS1 == b:
        cnt = count
        break
    for i in nextPos[zero]:
        tmpS1 = nextS1[:]
        tmpS1[i], tmpS1[zero] = tmpS1[zero], tmpS1[i]
        print(tmpS1)
        key = str(tmpS1)
        if key in visited:
            continue
        q.append([tmpS1, i, count + 1])
    print('------------------');

print(cnt)