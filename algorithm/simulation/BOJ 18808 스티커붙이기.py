# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
row, col, K = map(int, sys.stdin.readline().split())
stickers = []
for _ in range(K):
  s_row, s_col = map(int, sys.stdin.readline().split())
  tmp = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(s_row) ]
  stickers.append(tmp)
field = [ [0] * col for _ in range(row) ]

def contrast(sticker_index, i, j): 
  # contrast True면 함수 빠져나가기 전에 put_sticker 호출할 것
  sticker_row = len(stickers[sticker_index])
  sticker_col = len(stickers[sticker_index][0])
  if (i + sticker_row > row) or (j + sticker_col > col): return False
  else:
    for cx in range(sticker_row):
      for cy in range(sticker_col):
        if (stickers[sticker_index][cx][cy] == 1) and (field[(cx+i)][(cy+j)] == 1):
          return False
  put_sticker(sticker_index, i, j)
  return True

def put_sticker(sticker_index, i, j):
  global field
  sticker_row = len(stickers[sticker_index])
  sticker_col = len(stickers[sticker_index][0])
  for cx in range(sticker_row):
    for cy in range(sticker_col):
      if stickers[sticker_index][cx][cy] == 1:
        field[(cx+i)][(cy+j)] = 1
  return

def change_dir(sticker_index):
  global stickers
  sticker_row = len(stickers[sticker_index])
  sticker_col = len(stickers[sticker_index][0])
  tmp = [ [0] * sticker_row for _ in range(sticker_col) ]
  for ori_row in range(sticker_row):
    for ori_col in range(sticker_col):
      tmp[ori_col][(sticker_row - ori_row -1)] = stickers[sticker_index][ori_row][ori_col]
  
  stickers[sticker_index] = tmp

def search_used_in_laptop():
  # 사용된 칸 count하여 return
  used = 0
  for i in range(row):
    for j in range(col):
      if field[i][j] == 1: used += 1
  return used

for sticker_index in range(K):
  sticker_used = False
  for dir in range(4):
    if sticker_used == True: break
    if dir != 0: change_dir(sticker_index) # 회전 함수 호출
    for i in range(row):
      if sticker_used == True: break
      for j in range(col):
        if sticker_used == True: break
        if contrast(sticker_index, i, j) == True:
          sticker_used = True
          break
          
print(search_used_in_laptop())


# 15:40 시작
# 17:10 첫 채점 성공

# 각 스티커에 대해 회전 방향에 대해서 필드를 완전탐색 하는 방식으로 구현
# 시간복잡도 따져보고 2초안에 돌릴 수 있을거 같아서 이 방식 선택
# 로직 설계 -> 함수로 구조화 -> 해결