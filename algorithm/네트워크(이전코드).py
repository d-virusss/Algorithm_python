from collections import deque
def solution(n, computers):
    visited = [False] * n
    network_count = 0
    for i in range(n):
        if visited[i] == False:
            bfs(computers, i, visited)
            network_count += 1
    answer = network_count
    return answer

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while(queue):
        now_node = queue.popleft()
        for i, v in enumerate(graph[now_node]):
            if visited[i] == False and v == 1:
                queue.append(v)
                visited[i] = True