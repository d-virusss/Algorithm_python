# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
n = int(sys.stdin.readline())
score = [int(sys.stdin.readline().strip()) for _ in range(n)]
score = [0] + score
total = [0] * 305
total[1] = score[1]
total[2] = score[1] + score[2]
total[3] = max(score[1] + score[3], score[2]+score[3])
if n<4:
  print(total[n])
else:
  for i in range(4, n+1):
    total[i] = max(total[i-3]+score[i-1]+score[i], total[i-3]+score[i-2]+score[i], total[i-2]+score[i])
print(total[n])