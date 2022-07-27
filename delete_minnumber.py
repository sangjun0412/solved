arr = [4, 3, 2, 1]


def solution(arr):
    answer = []
    if len(arr) == 1:
        answer = [-1]
        return answer
    arr.remove(min(arr))
    return arr


print(solution(arr))
