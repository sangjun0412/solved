import copy


def solution(name):
    answer = 0
    list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cnt = []
    list2 = copy.deepcopy(list1)
    list2.sort(reverse=True)
    a_cnt = 0
    for i in range(0, len(name)):
        if list1.index(name[i]) < 13:
            cnt.append(int(list1.index(name[i])))
        else:
            cnt.append(int(list2.index(name[i]) + 1))

    return cnt


print(solution("JAN"))
