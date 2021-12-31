a,b,c,d = map(int, input().split())
e=c-a
f=d-b
if(a<b and a<e and a<f):
    print(a)
elif(b<a and b<e and b<f):
    print(b)
elif(e<a and e<b and e<f):
    print(e)
elif(f<a and f<b and f<e):
    print(f)
