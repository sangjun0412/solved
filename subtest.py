def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first_cnt = 0
    second_cnt = 0
    third_cnt = 0
    length = len(answers)
    answer = []

    for i in range(length):
        if answers[i] == first[i % 5]:
            first_cnt += 1
        if answers[i] == second[i % 8]:
            second_cnt += 1
        if answers[i] == third[i % 10]:
            third_cnt += 1
    if first_cnt >= second_cnt and first_cnt >= third_cnt:
        answer.append(1)
    if second_cnt >= first_cnt and second_cnt >= third_cnt:
        answer.append(2)
    if third_cnt >= first_cnt and third_cnt >= second_cnt:
        answer.append(3)

    return answer
