# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
from collections import deque
row, col = map(int, sys.stdin.readline().split())
field = [list(sys.stdin.readline().strip()) for _ in range(row)]
jihoon = [['#']*col for _ in range(row)]
fire = [['#']*col for _ in range(row)]
q = deque([])
for i in range(row):
	for j in range(col):
		if field[i][j] == 'J':
			q.append((i, j))
			jihoon[i][j] = 0
			while q:
				trow, tcol = q.popleft()
				cvalue = jihoon[trow][tcol]
				if trow-1 >= 0: # 위로 이동가능할 때
					if field[trow-1][tcol] != '#' and jihoon[trow-1][tcol] == '#':
						jihoon[trow-1][tcol] = cvalue + 1
						q.append((trow-1, tcol))
				if tcol-1 >= 0: # 좌로 이동가능할 떄
					if field[trow][tcol-1] != '#' and jihoon[trow][tcol-1] == '#':
						jihoon[trow][tcol-1] = cvalue + 1
						q.append((trow, tcol-1))
				if tcol+1 <= col-1: # 우로 이동가능할 때
					if field[trow][tcol+1] != '#' and jihoon[trow][tcol+1] == '#':
						jihoon[trow][tcol+1] = cvalue + 1
						q.append((trow, tcol+1))
				if trow+1 <= row-1: # 아래로 이동가능할 때
					if field[trow+1][tcol] != "#" and jihoon[trow+1][tcol] == '#':
						jihoon[trow+1][tcol] = cvalue + 1
						q.append((trow+1, tcol))

for i in range(row):
	for j in range(col):
		if field[i][j] == 'F':
			visited = [[False]*col for _ in range(row)]
			q.append((i, j))
			fire[i][j] = 0
			while q:
				trow, tcol = q.popleft()
				cvalue = fire[trow][tcol]
				if trow - 1 >= 0:  # 위로 이동가능할 때
					if field[trow - 1][tcol] != '#' and not visited[trow-1][tcol]:
						visited[trow-1][tcol] = True
						# 첫 불 계산할때는 옆이 다 벽, 그 이후에는 숫자가 있을텐데 그거보다 작을때만 업데이트 시킴
						if fire[trow-1][tcol] == '#' or fire[trow-1][tcol] > cvalue+1:
							fire[trow - 1][tcol] = cvalue + 1
							q.append((trow - 1, tcol))
				if tcol - 1 >= 0:  # 좌로 이동가능할 떄
					if field[trow][tcol - 1] != '#' and not visited[trow][tcol-1]:
						visited[trow][tcol-1] = True
						if fire[trow][tcol-1] == '#' or fire[trow][tcol-1] > cvalue+1:
							fire[trow][tcol - 1] = cvalue + 1
							q.append((trow, tcol - 1))
				if tcol + 1 <= col - 1:  # 우로 이동가능할 때
					if field[trow][tcol + 1] != '#' and not visited[trow][tcol+1]:
						visited[trow][tcol + 1] = True
						if fire[trow][tcol+1] == '#' or fire[trow][tcol+1] > cvalue+1:
							fire[trow][tcol + 1] = cvalue + 1
							q.append((trow, tcol + 1))
				if trow + 1 <= row - 1:  # 아래로 이동가능할 때
					if field[trow + 1][tcol] != "#" and not visited[trow+1][tcol]:
						visited[trow+1][tcol] = True
						if fire[trow+1][tcol] == '#' or fire[trow+1][tcol] > cvalue+1:
							fire[trow + 1][tcol] = cvalue + 1
							q.append((trow + 1, tcol))

time = 1000000000
for i in range(row):
	for j in range(col):
		if i == 0 or i == (row-1) or j == 0 or j == (col-1):
			if field[i][j] != '#' and jihoon[i][j] < fire[i][j] and jihoon[i][j] < time:
				time = jihoon[i][j]

if time == 1000000000:
	print("IMPOSSIBLE")
else:
	print(time+1)