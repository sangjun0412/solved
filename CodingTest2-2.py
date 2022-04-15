n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    minVal = 10001
    for a in data:
        minVal = min(minVal, a)
    result = max(result, minVal)

print(result)