from collections import Counter
def solution(clothes):
    clothes_count_list = list(Counter(list(map(lambda x : x[1], clothes))).values())
    answer = 1
    for i in clothes_count_list:
        answer = answer * (i+1)

    answer = answer - 1
    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
a = solution(clothes)
print(a)