from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = deque([0] * (bridge_length))
    truck_weights_q = deque(truck_weights)
    time = 0
    while q:
        time += 1
        q.popleft()
        if truck_weights_q:
            if sum(q) + truck_weights_q[0] <= weight:
                q.append(truck_weights_q.popleft())
            else:
                q.append(0)
    
    return time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

result = solution(bridge_length, weight, truck_weights)
print(result)

# 풀이 방법이 지저분한거 같아 검색, 도로를 직접 리스트로 구현하고 트럭들이 도로를 건너는 모습을 표현하여 풀이
# sum / pop(0)로 인하여 시간복잡도가 높은 편, sum을 다른 방법으롣 대체하고, pop(0)을 deque의 popleft()로 대체하면 좋을 것 같다.