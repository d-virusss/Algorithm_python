# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
from collections import deque

n = int(sys.stdin.readline())
picture = [list(sys.stdin.readline().strip()) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

q = deque()
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

normal_count = 0
disorder_count = 0

for row in range(n):
    for col in range(n):
        if not visit[row][col]:
            normal_count += 1
            visit[row][col] = 1
            pivot = picture[row][col]
            q.append((row, col))
            while q:
                cur_row, cur_col = q.popleft()
                for i in range(4):
                    nx = cur_row + drow[i]
                    ny = cur_col + dcol[i]
                    if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                        if picture[nx][ny] == pivot:
                            q.append((nx, ny))
                            visit[nx][ny] = 1

visit = [[0] * n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if not visit[row][col]:
            disorder_count += 1
            visit[row][col] = 1
            if picture[row][col] in ["R", "G"]:
                is_RG = True
            else:
                is_RG = False
            q.append((row, col))
            while q:
                cur_row, cur_col = q.popleft()
                for i in range(4):
                    nx = cur_row + drow[i]
                    ny = cur_col + dcol[i]
                    if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                        if is_RG:
                            if picture[nx][ny] == "R" or picture[nx][ny] == "G":
                                q.append((nx, ny))
                                visit[nx][ny] = 1
                        else:
                            if picture[nx][ny] == "B":
                                q.append((nx, ny))
                                visit[nx][ny] = 1

print(normal_count, end=' ')
print(disorder_count)

# 기본 BFS
# 감 안잡힐 때 이 문제 보고 BFS 감 잡자!
# visit를 q에 넣을 때 체크하고, 넣기 전에도 visit한 건 넣지 않도록 체크해야함
# 30분 소요