a,b,c,d = map(int, input().split())

e = c - a
f = d - b

numlist = [a,b,e,f]
small = min(numlist)
print(small)