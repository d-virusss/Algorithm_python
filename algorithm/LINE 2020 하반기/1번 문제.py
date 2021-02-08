# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
def solution(boxes):
    product = [0] * 100005
    for box in boxes:
        product[box[0]] += 1
        product[box[1]] += 1

    pair, no_pair = 0, 0
    for e in product:
        if e != 0:
            if e % 2 == 0:
                pair += 1
            elif e % 2 == 1:
                no_pair += 1

    return len(boxes)-pair

boxes = [[1,2], [2,3], [3,1]]
print(solution(boxes))

# += 헷갈려서 시간 조금 뺏김
# 15:35 ~ 15:50, 15분 소요