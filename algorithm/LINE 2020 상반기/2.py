# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
# 부정행위지수 문제

def solution(answer_sheet, sheets):
  result = 0
  for i in range(len(sheets)-1):
    for j in range(i+1,len(sheets)):
      wrong_count = 0
      sequence_count = 0
      longest_sequence = 0
      for q in range(len(answer_sheet)):
        if (sheets[i][q] == sheets[j][q]) and (sheets[i][q]!=answer_sheet[q]):
          wrong_count += 1
          sequence_count += 1
        else:
          if sequence_count > longest_sequence: longest_sequence = sequence_count
          sequence_count = 0
      if sequence_count > longest_sequence: longest_sequence = sequence_count
      if wrong_count+(longest_sequence**2) > result:
        result = wrong_count+(longest_sequence**2)

  return result

answer_sheet = "24551"
sheets = ["24553", "24553", "24553", "24553"]
print(solution(answer_sheet, sheets))

# 12:08 시작
# 12:24 중단
# 12:43 vscode 권한설정 완료, extension 정상작동
# 12:45 풀이시작
# 12:58 풀이 완료
# 30분 소요
# 마지막 문항만 의심문항인 경우가 있으므로 q 관련 for문 돌고나서도
# 한 번 체크해줘야 문제가 없음!

# 처음과 마지막 부근 예외처리를 잘하자