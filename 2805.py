N, M = map(int, input().split())
x = list(map(int, input().split()))
start, end = 1, max(x)
while start <= end:
    mid = (start+end)//2
    sum = 0
    for i in x:
        if i >= mid:
            sum += i - mid
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
