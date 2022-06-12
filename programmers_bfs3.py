from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    que = deque()
    que.append([begin, 0])

    while que:
        x, cnt = que.popleft()

        if x == target:
            return cnt

        for i in range(len(words)):
            diff = 0
            word = words[i]
            for j in range(len(x)):
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                que.append([word, cnt + 1])

    return 0
