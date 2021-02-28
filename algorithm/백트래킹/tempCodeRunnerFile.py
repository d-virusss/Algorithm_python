import sys
n, m = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
used = [False] * (n+1)
result = [0] * m
count = 0
print(n)
print(m)
print(numbers)
print(used)

def dfs(depth):
	global count
	if count == m:
		for num in result:
			print(num, end=' ')
		print('')
		return
	for i in range(depth, n):
		result[count] = numbers[i]
		used[count] = True
		count += 1
		dfs(depth+i)
		count -= 1
		used[count] = False

dfs(0)