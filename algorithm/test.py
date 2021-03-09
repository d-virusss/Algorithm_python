import sys
from collections import deque
dir = [[0], [0, 1, 2, 3], [0, 1], [0, 1, 2, 3], [0, 1, 2, 3], [0]]
cctv_count = 5
cctv = [3,2,5,5,1]
arr = [-1] * cctv_count
visited = [False] * cctv_count
count = 0
def dfs(depth):
    global arr, visited, count
    if depth == cctv_count:
        print(arr)
        count += 1
        return
    for i in range(len( dir[cctv[depth]] )):
        arr[depth] = (dir[cctv[depth]][i])
        visited[depth] = True
        dfs(depth+1)
        visited[depth] = False

dfs(0)

print(count)