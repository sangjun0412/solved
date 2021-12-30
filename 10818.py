x =input()
list1 = list(map(int, input().split()))
max=0
min=0
for i in list1:
    if(max<i):
        max=i
    if(min>i):
        min=i
print(min,max)