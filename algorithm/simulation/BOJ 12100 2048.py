# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
N = int(sys.stdin.readline())
origin = [ list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
drow = [1,0,-1,0] # 0이면 위로 움직일 때라서 -> 위에서부터 내려오면서 검사
dcol = [0,-1,0,1]
search_dir = [
	[0, 1],
	[1, 0],
	[0, 1],
	[1, 0]
]
start = [
	[0,0],
	[0, N-1],
	[N-1, 0],
	[0,0]
]
field = [[0]*N for _ in range(N)]
arr = [0] * 5
used = [False] * 5
result = -1
def move(dir): # 방향을 선택해주는 매개변수 받아야함, 0부터 시계방향
	global field
	for i in range(N):
		row = start[dir][0] + (search_dir[dir][0]*i)
		col = start[dir][1] + (search_dir[dir][1]*i)
		prev_val, prev_row, prev_col = 0, row, col
		for j in range(N):
			if field[row][col] != 0:
				if prev_val == 0: # 이전값이 없으면
					prev_val = field[row][col]
					prev_row = row
					prev_col = col
				else: # 이전값이 존재하면
					if field[row][col] == prev_val: # 현재 값과 비교해서 같으면
						field[prev_row][prev_col] = (field[row][col] * 2) # 이전 값 2배
						field[row][col] = 0 # 현재 값 0로 assign
						prev_val = 0 # prev_val 0 초기화
					else:
						prev_val = field[row][col] # 현재값이랑 다르면 내가 prev_val이 됨
						prev_row = row
						prev_col = col
			row = row + drow[dir]
			col = col + dcol[dir] # 총 4X4 이면 3번만 수행되면 됨
	remove_air(dir)

def remove_air(dir): # 방향 선택해주는 매개변수 받아야함
	global field
	for i in range(N):
		row = start[dir][0] + (search_dir[dir][0]*i)
		col = start[dir][1] + (search_dir[dir][1]*i)
		s_row = row
		s_col = col
		tmp = []
		for j in range(N):
			if field[row][col] != 0:
				tmp.append(field[row][col])
				field[row][col] = 0
			row = row + drow[dir]
			col = col + dcol[dir]
		for num in tmp:
			field[s_row][s_col] = num
			s_row = s_row + drow[dir]
			s_col = s_col + dcol[dir]

def init_field():
	for i in range(N):
		for j in range(N):
			field[i][j] = origin[i][j]

def search_max():
	global result
	now_max = 0
	for i in range(N):
		for j in range(N):
			if field[i][j] != 0:
				if field[i][j] > now_max: now_max = field[i][j]
	if now_max > result: result = now_max
	return

def dfs(depth):
	global count
	if depth == 5:
		for dir in arr:
			move(dir)
		search_max()
		init_field()
		return
	for i in range(4):
		arr[depth] = i
		dfs(depth + 1)

dfs(0)
print(result)

# 23:10 시작 / gold 2
# 25:14 첫번째 try -> 성공

# 로직은 24:00에 완성, 그러나 완성된 로직을 코드로 옮기는데 오래걸림
# 24:40 쯤 move & remove_air 테스트 완료
# 나머지 35분 동안 삽질
# readlin()으로 인한 오류(숫자 하나 받을땐 split 사용금지) 대략 15분 소모
# 백트래킹 이해 부족으로 인한 순열 만들고 테스트 하는데 시간 소모
# 오늘도 고생했다 용균아 꾸준히 하는 모습 good