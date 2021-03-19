# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-


def solution(maze):
  row = len(maze)
  col = len(maze[0])
  move_count = 0
  dx = [1,0,-1,0] # 하 우 상 좌 반시계 방향
  dy = [0,1,0,-1]
  dir = 0 # 0 1 2 3 하 우 상 좌 바라보는 방향
  x, y = 0, 0
  while True:
    left_dir = (dir+1)%4
    lx = x + dx[left_dir]
    ly = y + dy[left_dir]
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not (0<=lx<row and 0<=ly<col) or maze[lx][ly] == 1: # 왼쪽이 벽일 경우
      if 0<=nx<row and 0<=ny<col: # 앞이 maze 범위 안
        if maze[nx][ny] == 0: # 갈 수 있는 길이면 이동
          x, y = nx, ny
          move_count += 1
        else: dir = (dir-1)%4 # 범위 안인데 벽이면 반시계로 회전
      else: dir = (dir-1)%4 # 범위 밖이면 시계방향회전
    else: # 왼쪽이 벽이 아니면 반시계회전 후 한 칸 이동
      dir = (dir+1)%4
      x += dx[dir]
      y += dy[dir]
      move_count += 1
    if x == row-1 and y == col-1: break


  return move_count


maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]
print(solution(maze))

# 19:35분 시작
# 19:46 stop
# 19:50 re
# 20:18 solve

# 40분 소요