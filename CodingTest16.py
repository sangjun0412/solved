import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

d = [0]*100

d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
	d[i] = max(d[i-1], d[i-2] + 1)

print(d[n - 1])