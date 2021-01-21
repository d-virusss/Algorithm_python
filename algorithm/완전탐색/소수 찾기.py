from itertools import permutations


def solution(numbers):
    answer = 0
    check = [0] * 10000010
    for i in range(1, len(numbers) + 1):
        p = list(permutations(numbers, i))
        for num in p:
            ele = int("".join(num))
            check[ele] += 1
    for i in range(len(check)):
        if check[i] > 0:
            if check_prime(i):
                answer += 1

    return answer


def check_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    num_root = round(number**0.5) + 1
    for i in range(3, num_root, 2):
        if number % i == 0:
            return False
    return True

numbers = "011"
print(solution(numbers))

# 35분 소요
# 처음에는 만든 원소를 그대로 check_prime으로 확인하여
# answer의 값을 증가시켰지만 그럴 경우
# 같은 값이 나오면 count가 중복되는 문제가 있었음

# 그래서 배열을 충분히 만든 후 나온 횟수를 체크하여
# 한 번이라도 나온 수들만 check_prime에 넣어서
# 같은 수는 한 번만 check_prime으로 확인하여 answer를
# 증가시키도록 보장하여 해결



# 소수 판별하는 함수의 경우에는 한 번 봐두면 좋을 듯

# 사용한 방법 : Permutation, 소수 판별 사용