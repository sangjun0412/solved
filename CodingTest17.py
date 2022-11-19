import sys

t = int(sys.stdin.readline())
list1 = []
for i in range(t):
	list1.append(int(sys.stdin.readline()))

cnt1 = 0
cnt0 = 0
def fibonacci(n):
    global cnt1
    global cnt0
	if n == 1:
		cnt1 += 1
	elif n == 0:
		cnt0 += 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

for i in list1:
	print(fibonacci(i))
	

