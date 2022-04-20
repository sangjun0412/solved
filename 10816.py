def binary_search(array, target, start, end):
    if(start > end):
        return None
    mid = (start + end)//2
    if(array[mid] == target):
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
x = list(map(int, input().split()))
x.sort()
m = int(input())
target = list(map(int, input().split()))

cnt = {}

for i in x:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in target:
    print(binary_search(x, i, len(x) - 1), end=' ')
