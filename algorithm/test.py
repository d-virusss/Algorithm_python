import sys
from collections import deque
# field = [list(sys.stdin.readline()) for _ in range(3)]
# print(field)
abc()
def abc():
  print("abc called")
q = deque([1, 2, 3, 4, 5, 6])
i = 0
while i < len(q):
  if q[i] == 3:
    q.popleft()
    i = 0
  i += 1