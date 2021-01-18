def solution(citations):
    answer = 0
    pivot = max(citations)
    h = -1
    for i in range(pivot+1):
        count = 0
        for citation in citations:
            if citation >= i:
                count += 1
            else:
                continue
        if min(i, count) > h:
            h = min(i, count)
            
    answer = h
    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))

# 볼만한 풀이
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer
# 내림차순으로 정렬 후 enumerate를 이용하여 (enumerate는 리스트의 원소를 
# (index, value)의 tuple로 만들어줌)
# index값을 h회 이상 인용되었음을 나타내기 위해 사용
# min을 통해서 실제 인용값이랑 h회를 비교하여 작은값을 고르고 그 중 max값을 고름