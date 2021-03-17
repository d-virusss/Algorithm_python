# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
from collections import deque
import sys

tc = int(sys.stdin.readline())
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def fire():
  qlen = len(fire_q)
  for _ in range(qlen):
    x, y = fire_q.popleft()
    for dir in range(4):
      nx = x + dx[dir]
      ny = y + dy[dir]
      if (0<=nx<row) and (0<=ny<col):
        if field[nx][ny] == '.':
          field[nx][ny] = '*'
          fire_q.append((nx, ny))

def bfs():
  while dog_q:
    fire()
    qlen = len(dog_q)
    for _ in range(qlen):
      x, y = dog_q.popleft()
      for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if (0<=nx<row) and (0<=ny<col):
          if field[nx][ny] == '.' and dog_field[nx][ny] == 0:
            dog_field[nx][ny] = dog_field[x][y] + 1
            dog_q.append((nx, ny))
        else:
          print((dog_field[x][y]))
          return
  print("IMPOSSIBLE")

for _ in range(tc):
  col, row = map(int, sys.stdin.readline().split(" "))
  field = [list(map(str, sys.stdin.readline().strip())) for _ in range(row)]
  dog_field = [[0] * col for _ in range(row)]
  dog_q = deque()
  fire_q = deque()
  for i in range(row):
    for j in range(col):
      if field[i][j] == '*': fire_q.append((i,j))
      if field[i][j] == '@': 
        dog_q.append((i,j))
        field[i][j] = '.'
        dog_field[i][j]=1
  bfs()
  

# 23:35 시작
# 24:20 첫 제출 -> 메모리 초과
# 24:45 bfs 돌 때 visited둬서 여러번 안돌게 해야함 반드시!!!!
# 그래야 메모리 초과가 나지 않음

# 25:00 메모리 초과 안나는데 틀렸습니다 떠서 질문 올림