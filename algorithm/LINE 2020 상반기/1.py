# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
# 괄호문제

def solution(input): # 정상이면 괄호쌍의 수, 비정상이면 -1 출력
    count = 0
    stack = []
    for c in input:
        if c == '(' or c == '{' or c == '[' or c == '<':
            stack.append(c)
        elif c == ')' or c == '}' or c == ']' or c == '>':
            if len(stack) == 0: return -1
            else:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                    count += 1
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                    count += 1
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                    count += 1
                elif c == '>' and stack[-1] == '<':
                    stack.pop()
                    count += 1
                else:
                    return -1
    if len(stack) > 0: return -1

    return count


ex = '>_<'
print(solution(ex))

# 11:55 시작
# 12:07 완료
# python은 elif!
# 12분 소요