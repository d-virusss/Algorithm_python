from collections import deque
def solution(priorities, location):
    result = [0] * len(priorities)
    q = deque(priorities)
    count = 1
    i = -1
    while q:
        i += 1
        i = i % len(priorities)
        if priorities[i] == max(q):
            result[i] = count
            count += 1
            q.remove(priorities[i])
        else:
            continue
    return result[location]

priorities = [2, 1, 3, 2]
location = 2
answer = solution(priorities, location)
print(answer)

# count가 인쇄되는 순서를 나타내는 변수, q를 돌면서 q의 원소가 전부 사라질때까지 반복
# i는 계속 priorities의 원소를 가리키면서 q에서 삭제되어도 index를 올바르게 가리키도록 함
# max(q)와 비교하면서 max면 출력하고 q에서 제거, 아니면 다음 index로!
# 그렇게 해서 result라는 리스트의 인덱스는 priorities의 i번째 원소가 몇 번째로 출력되었나를
# 나타내게 된다