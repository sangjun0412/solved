import sys
import copy
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
y = list(set(x))
y.sort()
print(x)
print(y)
dic = {y[i]: i for i in range(len(y))}
print(dic)

for i in x:
    print(dic[i], end=' ')


# result = []

# for i in range(len(x)):
#     cnt = 0
#     for j in range(len(y)):
#         if x[i] > y[j]:
#             cnt += 1
#     result.append(cnt)
# for i in result:
#     print(i, end=' ')
# 시간초과
