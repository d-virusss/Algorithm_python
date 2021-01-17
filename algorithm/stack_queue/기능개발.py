# 40분 소요, pass 랑 continue 구분할 것
import collections as c
def solution(progresses, speeds):
    answer = []
    days = []
    for p, s in list(zip(progresses, speeds)):
        if (100-p)%s == 0:
            day = int((100-p)/s)
        else:
            day = int((100-p)/s)+1
        days.append(day)
    days_q = c.deque(days)
    print(days)
    count = 1
    pivot = -1
    for day in days:
        if pivot == -1:
            pivot = day
            pass
        if pivot >= day:
            count += 1
        else:
            answer.append(count)
            count = 1
            pivot = day
    answer.append(count)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
result = solution(progresses, speeds)
print(result)