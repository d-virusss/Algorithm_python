# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
# cony bank 문제

def solution(snapshots, transactions):
  executed = [False] * (len(transactions)+10)
  accounts = {}
  result = []
  for shot in snapshots:
    accounts[shot[0]] = int(shot[1])

  for t in transactions:
    if not executed[int(t[0])]:
      executed[int(t[0])] = True
      if t[2] in accounts:
        if t[1] == "SAVE":
          accounts[t[2]] += int(t[3])
        else: # WITHDRAW일 떄
          accounts[t[2]] -= int(t[3])
      else:
        accounts[t[2]] = int(t[3])

  for k, v in accounts.items():
    result.append([k, str(v)])
  
  result = sorted(result, key=lambda x:x[0])

  return result

snapshots = [
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"],
  ["ACCOUNT10", "150"]
]
transactions = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]

solution(snapshots, transactions)

# 13:10 시작
# 13:40 완료
# 30분 소요

# dictionary items / sorted 함수 숙지