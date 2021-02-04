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