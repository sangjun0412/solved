import sys

k, n = map(int, input().split())
x = []

for i in range(k):
    x.append(int(input()))

x.sort()
start = 1
end = x[-1]
print(end)
