def solution(begin, target, words):
    if target not in words:
        return 0
    isused = [0] * len(words)
    result = []  # 백트래킹 중 나오는 결과(count)값을 담아놓는 배열

    def can_change(begin, end):  # 두 단어가 바꿀 수 있는지 체크하는 함수
        diff_count = 0
        for i in range(len(begin)):
            if begin[i] != end[i]:
                diff_count += 1
        if diff_count == 1:
            return True
        else:
            return False

    def dfs(k, crnt_word):
        if crnt_word == target:
            result.append(k)
            return
        else:
            for i in range(len(words)):
                if isused[i] == 0 and can_change(crnt_word, words[i]):
                    isused[i] = 1
                    dfs(k + 1, words[i])
                    isused[i] = 0

    dfs(0, begin)
    answer = min(result)
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

# 백트래킹 이용하여 해결
# 바킹독 재귀, 백트래킹 참고한 시간 포함 2시간