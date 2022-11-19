import sys

n = int(sys.stdin.readline())
list1 = list(map(int, input().split()))
result = [0 for i in range(n)]
list1.sort()

for i in range(n):
    if i == 0:
        result[0] = min(list1)
    else:
        result[i] = result[i - 1] + list1[i]

answer = 0

for x in result:
    answer += x

print(answer)
