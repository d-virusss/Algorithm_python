# 13시 10분 시작
# 13시 19분 제출 // 효율 테스트 시간초과
# 13시 45분 다른 코드 참고하여 해결
# 30분 정도 counter / zip / hash에 대해 정리

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for par, com in zip(participant, completion):
        if par != com:
            return par

    answer = participant[-1]
        
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

ans = solution(participant, completion)
print(ans)