def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[j] >= prices[i]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer

prices = [1,2,3,2,3]
result = solution(prices)
print(result)