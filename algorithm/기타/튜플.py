# 16시 36분 시작
# 1시간?
# 다른문제 풀이로 Counter 모듈, list comprehension, filter, map
def solution(s):
    answer = []
    a = s.split('{')
    a.sort(key=len)
    i = 0
    start = 2
    while i<len(a)-2:
        for j in a[start].split(','):
            tmp = int(''.join([i for i in j if i.isdigit()]))
            if tmp not in answer:
                answer.append(tmp)
                break
        i += 1
        start += 1
    return answer
s = "{{20,111},{111}}"
ans = solution(s)
print(ans)