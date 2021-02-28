# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
from collections import deque
row, col = map(int, sys.stdin.readline().split())
field = [ list(sys.stdin.readline().strip()) for _ in range(row)]
q, fire_q = deque([]), deque([])
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
visit = [[0] * col for _ in range(row)]
time = 0
for r in range(row):
  for c in range(col):
    if field[r][c] == 'J':
      q.append((r,c))
      field[r][c] = '.'
      visit[r][c] = 1
    elif field[r][c] == 'F':
      fire_q.append((r,c))
      visit[r][c] = 1
while True:
  if len(fire_q) != 0:
    for _ in range(len(fire_q)):
      frow, fcol= fire_q.popleft()
      for i in range(4):
        nrow = frow + drow[i]
        ncol = fcol + dcol[i]
        if nrow >= 0 and nrow < row and ncol >= 0 and ncol < col:
          if field[nrow][ncol] == '.':
            field[nrow][ncol] = 'F'
            fire_q.append((nrow, ncol))
  if len(q) == 0:
    print("IMPOSSIBLE")
    sys.exit(0)
  else:
    time += 1
    for _ in range(len(q)):
      crnt_j_row, crnt_j_col = q.popleft()
      if crnt_j_row == 0 or crnt_j_row == (row-1) or crnt_j_col == 0 or crnt_j_col == (col-1):
        print(time)
        sys.exit(0)
      else:
        for i in range(4):
          jnrow = crnt_j_row + drow[i]
          jncol = crnt_j_col + dcol[i]
          if jnrow >= 0 and jnrow < row and jncol >= 0 and jncol < col:
            if field[jnrow][jncol] == '.' and not visit[jnrow][jncol]:
              visit[jnrow][jncol] = 1
              q.append((jnrow, jncol))

# BFS를 풀 때는 반드시 visit 배열을 활용하여 한번 지나온길을 또 방문하지 않도록 하자
# 사용한 방법
# 한 턴마다 불 bfs -> 지훈 bfs 순으로 돌린다
# 한 턴만큼만 반복하기 위해서 len(fire_q), len(q)만큼 반복을 한다.
# q에 원소가 하나라도 있으면(지훈이가 이동할 공간이 하나라도 있으면) time을 증가시키고, 가장자리의 경우에는 출력 / 아닌 경우에는 그 위치에서 순회
# q에 원소가 하나도 없는 경우에는 탈출할 공간이 없는 것이므로 IMPOSSIBLE을 출력하고 종료한다.