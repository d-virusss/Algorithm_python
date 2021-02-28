# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
input = int(sys.stdin.readline())
d = [0] * 1000010
for i in range(2,input+1):
	d[i] = d[i-1] + 1
	if i%2 == 0:
		d[i] = min(d[i], d[int(i/2)]+1)
	if i%3 == 0:
		d[i] = min(d[i], d[int(i/3)]+1)

print(d[input])


# import sys
# from collections import deque
# q = deque([])
# input = int(sys.stdin.readline())
# result = []
# q.append((input, 0))
# while q:
# 	num, count = q.popleft()
# 	if num == 1:
# 		result.append(count)
# 	else:
# 		if num%3 == 0:
# 			q.append((int(num/3), count+1))
# 		if num%2 == 0:
# 			q.append((int(num/2), count+1))
# 		q.append((num-1, count+1))

# print(min(result))

# 처음 풀 때, bfs로 풀었음 -> 메모리 초과