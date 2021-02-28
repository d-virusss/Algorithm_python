# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-

def solution(companies, applicants):
    def to_int(char):
        if char.isdigit():
            return int(char)
        else:
            return char

    def matching():
        nonlocal match_list
        count = 0
        for index, company_name in enumerate(match_list):
            tmp_list = match_list[company_name]
            match_list[company_name] = ''
            for a_priority_applicant in companies[index][1]:
                if count == companies[index][2]:
                    count = 0
                    break
                if a_priority_applicant in tmp_list:
                    match_list[company_name] += a_priority_applicant
                    count += 1

    def matched():
        nonlocal match_list
        tmp = ""
        for i in match_list:
            tmp += match_list[i]
        return tmp

    companies = [list(map(to_int, x.split(' '))) for x in companies]
    applicants = [list(map(to_int, x.split(' '))) for x in applicants]
    max_range = max(applicants, key=lambda x:x[2])[2]
    match_list = {}
    for com in companies:
        match_list[com[0]] = ''

    for i in range(1, max_range+1):
        matched_list = matched()
        for person in applicants:
            if person[2] >= i and person[0] not in matched_list:
                match_list[person[1][i-1]] += person[0]
        matching()

    result = []
    for com in match_list:
        match_list[com] = "".join(sorted(match_list[com]))
        result.append(com+'_'+match_list[com])
    return result


companies = ["A abc 2", "B abc 1"]
applicants = ["a AB 1", "b AB 1", "c AB 1"]
print(solution(companies, applicants))

# 19:15 ~ 20:30 + 집에서 5분
# dictionary의 key는 immutable, value는 mutable하다
# map(함수, iterable)
# filter(함수, iterable)
# 파이썬에서의 LEGB 원칙 기억할 것
# inner func에서 outer func의 변수를 사용하려면 nonlocal 사용
# max(iterable, key(option))
