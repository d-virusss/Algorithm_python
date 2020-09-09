from collections import Counter

def solution(genres, plays):
    answer = []
    counter = Counter()
    for i in range(len(genres)):
        tmp = Counter({genres[i]:plays[i]})
        counter += tmp
    dict_matched = dict(counter)
    genre_ranking = list(map(lambda x : x[0], sorted(dict_matched.items(), key=lambda x : x[1], reverse=True )))
    a = [(i, genres[i], plays[i]) for i in range(len(genres))]
    sub = sorted(a, key=lambda x:x[2], reverse=True)
    for i in genre_ranking:
        count=0
        for j in sub:
            if count == 2:
                break
            if i == j[1]: 
                answer.append(j[0])
                count += 1

    return answer

a = ["jazz", "jazz", "hiphop", "hiphop", "classic", "pop"]
b = [2000, 2000, 850, 850, 800, 2500]
sol = solution(a, b)
print(sol)