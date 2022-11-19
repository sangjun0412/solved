n = list(input())
n.sort(reverse=True)
print(n)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 == 0 and '0' in n:
    print(''.join(n))
else:
    print(-1)
