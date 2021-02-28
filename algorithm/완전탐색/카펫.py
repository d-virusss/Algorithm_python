def solution(brown, yellow):
    answer = []
    y_num = []
    max_y = round(yellow**0.5) + 1
    for i in range(1, max_y):
        if yellow % i == 0:
            y_num.append(i)

    x, y = 0, 0

    for i in y_num:
        y = i
        x = int(yellow / y)
        if brown == 2 * x + 2 * y + 4:
            answer.append(x + 2)
            answer.append(y + 2)
            break

    return answer

# 대략 25분 소요(집중하면 더 줄일 수 있을 듯함)

# 사용한 알고리즘
# yellow의 약수를 y_num에 저장 후
# y_num 순회하면서 가로 세로 구하고 그 가로 세로일 때의 겉넓이를 구해서 brown과 비교, 매치되면 return 함

# 다시 볼만한 사항 : 약수 구하는 방법 정도!