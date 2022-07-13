n = 118372


def solution(n):
    answer = ""
    change = str(n)
    list1 = []

    for i in change:
        list1.append(i)

    list1.sort(reverse=True)
    for i in list1:
        answer += str(i)
    answer = int(answer)
    return answer


print(solution(n))
