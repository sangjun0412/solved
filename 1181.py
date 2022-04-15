a = int(input())
l1 = []
for _ in range(a):
    l1.append(input())
l1 = set(l1)
l1.sort()
l1.sort(key=len)

for i in l1:
    print(i)