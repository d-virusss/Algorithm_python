# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-

import sys
num, len_seq = map(int,(sys.stdin.readline().split()))
seq = list(map(int, sys.stdin.readline().split()))
seq = sorted(seq)

ftd_seq = []
for i in seq:
  if not ftd_seq:
    ftd_seq.append(i)
  else:
    if ftd_seq[-1] != i:
      ftd_seq.append(i)

depth = 0
answer = [0] * len_seq
used = [False] * num

def dfs():
  global depth
  if depth == len_seq:
    for val in answer:
      print(val, end=' ')
    print('')
    return
  for i in range(num):
    if used[i] == False:
      used[i] = True
      answer[depth] = seq[i]
      depth += 1
      dfs()
      used[i] = False
      depth -= 1

dfs()

# 시작 시간 19:00