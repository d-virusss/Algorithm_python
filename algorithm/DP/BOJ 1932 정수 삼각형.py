# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-

import sys
row = int(sys.stdin.readline())
stair = [0]
for i in range(1, row+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    stair.append(tmp)

answer = [-1]
answer.append(stair[1]) # answer[n]은 최상단부터 n층만큼 내려왔을 때 가장 최적경로로 왔을 때의 합 나타냄

for i in range(2, row+1):
  answer.append([])
  for index, val in enumerate(stair[i]):
    if index == 0:
      answer[i].append(answer[i-1][index]+val)
    elif index == len(stair[i])-1:
      answer[i].append(answer[i-1][index-1]+val)
    else:
      answer[i].append(max(answer[i-1][index-1], answer[i-1][index])+val)

print(max(answer[row]))

# 시작 시간 18:10
# 종료 시간 18:48
# 38분 소요

# 풀이 방법
# answer[n]은 최상층을 첫째줄이라 할 때, n번째 줄까지 오면서 만들 수 있는 최대 합 나타냄, 원소는 n개
# answer[1]은 최상층 의 값 그대로
# answer[3]은 3층까지 오면서 만들 수 있는 최대 값, 원소는 3개
# index가 처음 혹은 끝일 때는 바로 위층의 answer 값을 더하고 중간 값인 경우에는 두 개중 max를 골라서
# 현재 val과 더하면서 answer를 채워간다.