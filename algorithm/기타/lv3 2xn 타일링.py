from itertools import combinations
def solution(n):
  first, second = 1, 1
  for i in range(n):
    first, second = second, first+second
  return first%1000000007

n = 60000
print(solution(n))