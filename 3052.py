cnt = 0
compare = [0]*10
for _ in range(10):
    i = int(input())
    s=i%42
    compare[s] += 1

print(compare)
