def solution(array, commands):
    answer = []
    tmp = []
    for i in range(len(commands)):
        tmp = sorted(array[(commands[i][0]-1):commands[i][1]])
        answer.append(tmp[commands[i][2]-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [
    [2, 5, 3],
    [4, 4, 1],
    [1, 7, 3]
]

result = solution(array, commands)
print(result)

# sort는 list 자체를 변경하는 것, sorted는 변경한 후 리스트를 반환한다.
# tmp 와 같이 임시 리스트를 쓸때는 sorted를 사용하자.
# tmp 이용하여 정렬 후 그대로 answer 리스트에 삽입하여 해결