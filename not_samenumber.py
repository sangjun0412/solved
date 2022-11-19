from collections import deque
arr = [1, 1, 3, 3, 0, 1, 1]


def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    change = deque(arr)
    answer.append(change.popleft())
    while change:
        tmp = change.popleft()
        if answer[-1] != tmp:
            answer.append(tmp)

    return answer


print(solution(arr))
