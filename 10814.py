n = int(input())
member_list = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_list.append((age, name))

member_list.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(member_list[i][0], member_list[i][1])
