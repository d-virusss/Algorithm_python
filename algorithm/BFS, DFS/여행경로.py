def solution(tickets):
    answer = ["ICN"]
    sorted_tickets = sorted(tickets, key=lambda x: x[1])
    start = "ICN"

    def can_go(idx):
        if len(sorted_tickets) == 1:
            return True
        for k in range(len(sorted_tickets)):
            if sorted_tickets[idx][1] == sorted_tickets[k][0]:
                return True
        return False

    while sorted_tickets:
        for i in range(len(sorted_tickets)):
            if sorted_tickets[i][0] == start and can_go(i):
                start = sorted_tickets[i][1]
                answer.append(sorted_tickets[i][1])
                sorted_tickets.pop(i)
                break
    return answer


tickets = [
	['ICN', 'SFO'],
	['SFO', 'ICN'],
	['ICN', 'SFO'],
	['SFO', 'QRE']
]

print(solution(tickets))

# 케이스 1번 시간초과, 정확도 75%