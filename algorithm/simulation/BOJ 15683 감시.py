# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
row, col = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(row)]
const_field = [[-1] * col for _ in range(row)]
for i in range(row):
  for j in range(col):
    const_field[i][j] = field[i][j]
shoot_dir = [
  [0],
  [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]],
  [[1,0,1,0], [0,1,0,1]],
  [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]],
  [[1,1,0,1], [1,1,1,0], [0,1,1,1], [1,0,1,1]],
  [[1,1,1,1]]
]
dir = [
  [0],
  [0, 1, 2, 3],
  [0, 1],
  [0, 1, 2, 3],
  [0, 1, 2, 3],
  [0]
]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cctv_count = 0
cctv = []
for i in range(row):
  for j in range(col):
    if 0 < field[i][j] < 6:
      cctv.append(field[i][j])
      cctv_count += 1
arr = [0] * cctv_count
visited = [False] * cctv_count
unsearched = 64

def shoot(cx, cy, dir):
  global field
  for i in range(4):
    if dir[i] > 0:
      nx = cx + dx[i]
      ny = cy + dy[i]
      while 0 <= nx < row and 0 <= ny < col:
        if field[nx][ny] != 6:
          if field[nx][ny] != "#" and not 0 < field[nx][ny] < 6:
            field[nx][ny] = '#'
          nx += dx[i]
          ny += dy[i]
        else:
          break
        
def count_unsearched():
  global unsearched
  result = 0
  for i in range(row):
    for j in range(col):
      if field[i][j] == 0:
        result += 1
  if unsearched > result:
    unsearched = result
  return

def clear_field():
  global field
  for i in range(row):
    for j in range(col):
      field[i][j] = const_field[i][j]

def search():
  now_cctv = 0
  for i in range(row):
    for j in range(col):
      if field[i][j] != "#" and 0 < field[i][j] < 6: # cctv를 만난 경우
        shoot(i, j, shoot_dir[cctv[now_cctv]][arr[now_cctv]])
        now_cctv += 1
  count_unsearched()
  clear_field()

def dfs(depth):
  global arr, visited
  if depth == cctv_count:
    search()
    return
  for i in range(len( dir[cctv[depth]] )):
    arr[depth] = (dir[cctv[depth]][i])
    visited[depth] = True
    dfs(depth+1)
    visited[depth] = False

dfs(0)
print(unsearched)

# 23:00 ~ 24:30 완료
# 백트래킹 이용하여 순열 구한 후
# 순열에 맞게 field 서치하면서 unsearched 구하고 비교
# 주요 포인트 : 백트래킹을 이용한 완전탐색 & 물대포 쏘듯이 table 정해놓고 슈팅하는 시뮬레이션 기법