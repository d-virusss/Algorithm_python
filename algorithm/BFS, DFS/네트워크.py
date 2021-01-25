from collections import deque


def solution(n, computers):
    answer = 0
    checked = [0] * n
    q = deque([])
    for i in range(n):
        if checked[i] == 0:
            q.append(i)
            while (q):
                node = q.popleft()
                checked[node] = 1
                for j in range(n):
                    if computers[node][j] == 1 and checked[j] == 0:
                        q.append(j)
            answer += 1
    return answer


n = 4
computers = [
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 1],
]
print(solution(n, computers))

# bfs로 해결
# 대각선을 기준으로 대칭일거라 생각해서 효율적으로 탐색하기 위해
# j in range(node+1, n)으로 했다가 30분 날림
# 실제해결시간은 15분 남짓
# 문제를 왤케 헷갈리겍 만드니...화나게