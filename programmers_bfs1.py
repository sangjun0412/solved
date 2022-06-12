from collections import deque


def bfs(numbers, target):
    answer = 0
    que = deque()
    n = len(numbers)
    que.append(numbers[0], 0)
    que.append(-1*numbers[0], 0)
    while que:
        tmp, idx = que.popleft()
        idx += 1
        if idx < n:
            que.append([tmp+numbers[idx], idx])
            que.append([tmp-numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer
