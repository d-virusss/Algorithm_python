# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
# 리눅스 쉘 명령어

def solution(directory, command):
  for c in command:
    what = c.split(" ")[0]
    if what == "cp":
      what, source, dest = c.split(" ")
    else:
      what, target = c.split(" ")
    if what == "mkdir":
      directory.append(target)
    elif what == "rm":
      for dir in directory[:]:
        if dir.startswith(target):
          directory.remove(dir)
    elif what == "cp":
      sub = source.split("/")[-1]
      for dir in directory[:]:
        if sub in dir:
          rest = dir.split(sub)[-1]
          directory.append(dest+sub+rest)

  directory = sorted(directory)

  return directory

directory = [
"/"
]
command = [
"mkdir /a",
"mkdir /a/b",
"mkdir /a/b/c",
"cp /a/b /",
"rm /a/b/c"
]

print(solution(directory, command))

# 13:40 시작
# 14:13 중단
# 14:20 시작
# 14:25 완료
# 40분 소요

# loop에서 원소를 삭제할 때는 원본 배열에서 돌지 말고
# directory[:] 처럼 복사(shallow copy)한 배열에서 순회하면서
# 삭제만 원본배열에서 진행하자

# 1차원 배열일떄는 [:] 이용,
# 2차원 부터는 import copy 모듈의 copy.deepcopy()를 사용하자