def binary_search(array, target, start, end):
    if(start > end):
        return None
    mid = (start + end)//2
    if(array[mid] == target):
        return mid
    elif(array[mid] > target):
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
x = list(map(int, input().split()))
x.sort()
m = int(input())
y = list(map(int, input().split()))

for i in y:
    result = binary_search(x, i, 0, n-1)
    if(result != None):
        print("yes", end=' ')
    else:
        print("no", end=' ')
