# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
from collections import deque
N = int(sys.stdin.readline())
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
for _ in range(N):
  col, row = map(int, sys.stdin.readline().split(" "))
  field = [ list(sys.stdin.readline().strip().split()) for _ in range(row) ]
  fire_field = [[0]*col for _ in range(row)]
  dog_field = [[0]*col for _ in range(row)]
  for i in range(row):
    for j in range(col):
      fire_field[i][j] = field[i][0][j]
      dog_field[i][j] = field[i][0][j]
  fire_visited = [ [False] * col for _ in range(row) ]
  dog_visiied = [[False]*col for _ in range(row)]
  fire_q = deque([])
  dog_q = deque([])
  impossible = False
  possible = False
  move_count = 0

  def init_visited():
    for i in range(row):
      for j in range(col):
        fire_visited[i][j] = False
        dog_visiied[i][j] = False
  
  def bfs():
    for i in range(row):
      for j in range(col):


  def fire_bfs():
    for i in range(row): # 불 bfs
      for j in range(col):
        if (fire_field[i][j] == '*') and (not fire_visited[i][j]):
          fire_visited[i][j] = True
          fire_q.append((i, j))
    while fire_q:
      crow, ccol = fire_q.popleft()
      for dir in range(4):
        nrow = crow + drow[dir]
        ncol = ccol + dcol[dir]
        if (0 <= nrow < row) and (0 <= ncol < col):
          if (not fire_field[nrow][ncol] == "#"):
            fire_field[nrow][ncol] = '*'

  def dog_bfs():
    global impossible
    dog_count = 0
    disabled_dog = 0
    for i in range(row):
      for j in range(col):
        if dog_field[i][j] == "@": dog_count += 1

    for i in range(row): # 상근이 bfs
      for j in range(col):
        if (dog_field[i][j] == '@') and (not dog_visiied[i][j]):
          dog_visiied[i][j] = True
          dog_q.append((i, j))
    while dog_q:
      crow, ccol = dog_q.popleft()
      around = 0
      for dir in range(4):
        nrow = crow + drow[dir]
        ncol = ccol + dcol[dir]
        if (0 <= nrow < row) and (0 <= ncol < col):
          if (dog_field[nrow][ncol] == ".") and (not dog_visiied[nrow][ncol]):
            dog_field[nrow][ncol] = '@'
            dog_visiied[nrow][ncol] = True
            around += 1
      if around == 0: disabled_dog += 1

    if dog_count == disabled_dog:
      impossible = True
  
  def contrast():
    global possible
    global impossible
    for i in range(row):
      for j in range(col):
        if dog_field[i][j] == '@' and fire_field[i][j] == '*':
          dog_field[i][j] = '*'
    leaved_dog = 0
    for i in range(row):
      for j in range(col):
        if dog_field[i][j] == '@': leaved_dog += 1
        if (i == 0) or (i ==(row-1)) or (j == 0) or j == (col-1):
          if dog_field[i][j] == '@':
            possible = True
    if leaved_dog == 0:
      impossible = True

  while(1):
    if possible:
      print(move_count+1)
      break
    fire_bfs()
    dog_bfs()
    contrast()
    if impossible: 
      print("IMPOSSIBLE")
      break
    init_visited()
    move_count += 1

# 23:15 시작
# 24:44 첫 제출 -> 시간초과
# 내일 다시 풀자