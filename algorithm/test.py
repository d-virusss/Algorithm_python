import sys
from collections import deque

stickers = [
  [
    [1,1,1,1,1],
    [0,1,1,1,0],
    [1,1,0,1,1],
  ]
]

def change_dir(sticker_index):
  global stickers
  sticker_row = len(stickers[sticker_index])
  sticker_col = len(stickers[sticker_index][0])
  tmp = [ [0] * sticker_row for _ in range(sticker_col)]
  for ori_row in range(sticker_row):
    for ori_col in range(sticker_col):
      tmp[ori_col][(sticker_row - ori_row - 1)] = stickers[sticker_index][ori_row][ori_col]

  stickers[sticker_index] = tmp

# change_dir(0)
a = [
  [1, 2, 3, 4, 5],
  [2, 3, 5, 6],
  [-1, 0, 5, 6],
  [56, 8, 3, 2],
  [1, 2, 5, 5, 6]
]
tmp = []
for i in range(1, 4):
  for j in range(i+1, 4):
    tmp.append((i,j))

print(tmp)

# print(stickers[0])