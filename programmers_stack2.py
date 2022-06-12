def solution(priorities, location):
    answer = 0
    max_num = max(priorities)
    while True:
        tmp = priorities.pop(0)
        if max_num == tmp:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_num = max(priorities)
        else:
            priorities.append(tmp)
            if location == 0:
                location = len(location) - 1
            else:
                location -= 1

    return answer
