# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
test_count = int(sys.stdin.readline())
result = []
def solution(student_num, select):
  solo = 0
  for i in range(1, student_num+1):
    group = []
    if not visited[i]:
      visited[i] = 1
      group.append(i)
      target = i
      check = True
      while check:
        target = select[target]
        if not visited[target]:
          visited[target] = 1
          group.append(target)
        elif target in group:
          # cycle 찾고 제외된 애들 수 만큼 solo 수 증가
          start_index = group.index(target)
          cycle = group[start_index:]
          solo += len(group) - len(cycle)
          check = False
        else:
          # 선택됐던 학생이면 group의 수 만큼 solo 카운트 증가
          solo += len(group)
          check = False
  result.append(solo)
      
      
for _ in range(test_count):
  student_num = int(sys.stdin.readline())
  select = list(map(int, sys.stdin.readline().split()))
  select = [0] + select
  visited = [0] * (student_num+1)
  solution(student_num, select)

for answer in result:
  print(answer)


# visited를 이용하여 방문하지 않은 경우에만 탐색 시작
# target을 쭉 따라가면서 target이 not visited인 경우에는 group에 추가
# visited인 경우에는 target이 group내에 있는 경우 -> cycle 찾아서 solo 수 증가
# target이 group에 없고 이미 visited이므로 group내의 학생들은 전부 팀을 만들 수 없으므로 solo 수 증가
# 테스트 케이스 수 만큼 반복한다.