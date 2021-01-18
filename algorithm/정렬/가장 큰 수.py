def solution(numbers):
    answer = ''
    s_num = []
    for num in numbers:
        s_num.append(str(num))
    s_num.sort(reverse=True)
    print(s_num)
    pivot = s_num[0][0]
    tmp = []
    for ele in s_num:
        is_good = True
        if ele[0]!=pivot:
            for s in tmp:
                answer += s
            pivot = ele[0]
            tmp = []
        if len(ele)==1:
            answer += ele
        else:
            for s in ele:
                if s<pivot:
                    tmp.append(ele)
                    is_good = False
                    break
                else:
                    continue
            if is_good:
                answer += ele
            else:
                continue
    if len(tmp):
        for s in tmp:
            answer += s
    
    if s_num[0][0] == '0':
      answer ='0'
    return answer

numbers = [12, 121]
print(solution(numbers))

# def solution(numbers):
#     answer = ''
#     s_num = list(map(str, numbers))
#     sorted_num = sorted(s_num, key=lambda x:x*3, reverse=True)
#     for x in sorted_num:
#         answer += x
#     return answer if int(answer) != 0 else "0"

# 내가 한 알고리즘의 경우 순환하며 서로 겹치는 12, 121과 같은 예시는 올바른 답이 나오지 않음
# 처음 생각한 알고리즘 : str으로 정렬한 후 pivot을 두고 pivot보다 작은 값을 갖는
# 원소가 ele에 포함되어 있는 경우 tmp에 저장하고 pivot이 바뀔 때 전부 answer에 붙여넣는다.
# 아래에 주석처리된 코드가 구글링을 통해 찾은 합리적인 정답
# numbers의 원소는 0 이상 1,000이하라는 조건이 있으므로
# str*3과 reverse 옵션을 이용하여 큰 값부터 내림차순으로 정렬한다.