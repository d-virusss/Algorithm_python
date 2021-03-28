# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
from collections import deque
row, col = map(int, sys.stdin.readline().split(" "))
field = [list(map(str, sys.stdin.readline().strip())) for _ in range(row)]
field = [list(map(int, a_row)) for a_row in field ]
count_field = [[0] * col for _ in range(row)]
visited = [[False] * col for _ in range(row)]
q = deque()
stop_sign = False
dx = [-1,0,1,0] # row
dy = [0,1,0,-1] # col
result = -1

def init_fields():
  global visited
  global count_field
  for i in range(row):
    for j in range(col):
      visited[i][j] = False
      count_field[i][j] = 0
      
def bfs():
  init_fields()
  global result
  global stop_sign
  global count_field
  count = 0
  q.append((0,0))
  visited[0][0] = True
  count_field[0][0] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < row and 0 <= ny < col:
        if field[nx][ny] == 0 and not visited[nx][ny]:
          visited[nx][ny] = True
          q.append((nx, ny))
          count_field[nx][ny] = count_field[x][y] + 1
          if nx == (row-1) and ny == (col-1) and count_field[nx][ny] > result:
            result = count_field[nx][ny]; stop_sign = True

for i in range(row):
  for j in range(col):
    if field[i][j] == 1:
      field[i][j] = 0
      bfs()
      if stop_sign: print(result); sys.exit(0)
      field[i][j] = 1

print(result)

# 12:25분 시작
# 12:45 첫 제출 -> 시간초과 // 왜 시간복잡도 생각을 안했을까.. 내일 다시 풀자
# 벽 부술수 있는 카운트, 현재까지의 거리 카운트트 한 tuple 큐에 넣어서 bfs 하기