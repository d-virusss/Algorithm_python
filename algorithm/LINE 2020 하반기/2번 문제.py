# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
from collections import deque
def solution(ball, order):
	q = []
	ball = deque(ball)
	result = []

	def hold_solve():
		i = 0
		while i < len(q):
			if q[i] == ball[0]:
				result.append(q.pop(i))
				ball.popleft()
				i = 0
			elif q[i] == ball[-1]:
				result.append(q.pop(i))
				ball.pop()
				i = 0
			else:
				i += 1
				
	for each_order in order:
		if ball[0] == each_order:
			result.append(ball.popleft())
			hold_solve()
		elif ball[-1] == each_order:
			result.append(ball.pop())
			hold_solve()
		else:
			q.append(each_order)


	return result


ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]
print(solution(ball, order))

# 15:55분 ~