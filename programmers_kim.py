seoul = ["Jane", "Kim"]


def solution(seoul):
    answer = ''
    result = seoul.index("Kim")
    answer = '김서방은 '+str(result)+"에 있다"
    return answer


print(solution(seoul))
