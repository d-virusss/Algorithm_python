# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
from collections import deque
subin, sister = map(int, sys.stdin.readline().split())
q = deque([subin])
time = [0] * 100010
while q:
    now = q.popleft()
    if now==sister:
        print(time[now])
        sys.exit(0)
    for next in (now-1, now+1, now*2):
        if 0 <= next <= 100000 and not time[next]:
            if next == now*2 and not now == 0:
                q.appendleft(next)
                time[next] = time[now]
            else:
                q.append(next)
                time[next] = time[now] + 1

# bfs 문제
# bfs는 q에 같은 시기에 들어간 원소들은 같은 거리 값(혹은 시간)을 갖는데 이 문제는 그렇지 않은 부분이 있어서 appendleft를 통해 우선적으로
# deque에 삽입하여 해결함, 메모리 관리를 위해 visited를 check할 필요가 있음! 이 문제에서는 time 배열을 이용하여 다목적으로 이용함
