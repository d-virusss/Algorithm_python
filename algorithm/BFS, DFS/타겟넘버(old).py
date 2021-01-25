from itertools import product as p


def solution(numbers, target):
    answer = 0
    count = 0
    operators = ['p', 'm']
    for i in p(operators, repeat=len(numbers)):
        tmp_val = 0
        for index, op in enumerate(i):
            if op == 'p':
                tmp_val += numbers[index]
            else:
                tmp_val -= numbers[index]
            if index == len(numbers) - 1:
                if tmp_val == target:
                    count += 1

    answer = count

    return answer

# bfs, dfs 문제이지만 product(중복 곱)가 먼저 떠올라 product로 해결했다.

# 참고할만한 코드

# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)

# product(*l) 과 같이 작성하면 l의 원소들을 unpacking 한다는 의미
# l = [(1, -1), (1, -1), (1, -1), (1, -1), (1, -1)] 인데
# product((1, -1), ... , (1, -1)) 이다
# 즉, product(*l)은, product(l[0], repeat=5)와 같다.
