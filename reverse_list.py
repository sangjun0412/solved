n = 10000000000000000000005


def solution(n):
    n = str(n)
    answer = []
    for i in range(len(n) - 1, 0, -1):
        answer.append(int(n[i]))

    return answer


print(solution(n))
