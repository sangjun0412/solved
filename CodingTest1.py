N, M, K = map(int, input().split())
N_list = list(map(int, input().split(' ')))
N_list.sort()

first = N_list[N - 1]
second = N_list[N - 2]
result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)