# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-

def solution(n):
  result = []
  def dfs(num, add_count):
    if num < 10:
      result.append([add_count, num])
      return
    num = str(num)
    for i in range(1,len(num)):
      if num[i] == '0':
        continue
      crnt_num = int(num[:i]) + int(num[i:])
      dfs(crnt_num, add_count+1)

  dfs(n, 0)

  result = sorted(result)
  return result[0]

n = 10007
print(solution(n))

# 16:55 ~ 17:20, 35분 소요