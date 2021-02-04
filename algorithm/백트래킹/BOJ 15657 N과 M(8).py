# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
n, m = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
used = [False] * (n+1)
result = [0] * m
depth = 0

def dfs(start):
	global depth
	if depth == m:
		for num in result:
			print(num, end=' ')
		print('')
		return
	for i in range(start, n):
		result[depth] = numbers[i]
		used[depth] = True
		depth += 1
		dfs(i)
		depth -= 1
		used[depth] = False

dfs(0)

# 백준에서 채점할때는 print 내용 조심할 것
# 수열의 관계식을 세워서 재귀를 부를 때 신경쓰자!