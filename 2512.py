import sys
n = int(sys.stdin.readline())

list1 = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

list1.sort()

def binary_search(arr, target, start, end):
	while(start <= end):
		mid = (start + end) // 2
		answer = 0
		for i in arr:
			if i <= mid:
				answer += i
			else:
				answer += mid
		if answer == target:
			return mid
		elif answer > target:
			end = mid - 1
		else:
			start = mid + 1

print(binary_search(list1, m, 0, list1[n-1]))
			