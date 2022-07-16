

def solution(people, limit):
    people.sort(reverse=True)
    cnt = 0

    for i in people:
        print("test"+str(i))
        if limit - i >= people[-1]:
            print("if"+str(i))
            people.remove(people[0])
            people.remove(people[-1])
            cnt += 1
        else:
            print("else" + str(i))
            people.remove(people[0])
            cnt += 1
    return cnt


print(solution([70, 50, 80], 100))
