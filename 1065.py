n = int(input())
count = 0

for i in range(1, n+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        count += 1
    elif num_list[2] - num_list[1] == num_list[1] - num_list[0]:
        count += 1
print(count)
