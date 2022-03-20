def solution(match, myLoc, oppLoc):
    ans = 0

    l = [0] * (max(match) + 1)
    r = [0] * (max(match) + 1)

    for idx, i in enumerate(match):
        if l[i] == 0:
            l[i] = idx
        else:
            r[i] = idx

    print(l)
    print(r)

    while(myLoc != oppLoc):
        myLoc = match[myLoc]
        oppLoc = match[oppLoc]

        if l[myLoc] != 0 and r[myLoc] != 0:
            ans += 1
    print(ans)


matches = [-1, 0, 0, 1, 2, 2, 3, 3, 4,4, 5, 5,6, 7, 8, 8, 9, 10, 10, 11, 11]
me = 16
opp = 13