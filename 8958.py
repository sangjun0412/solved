x = int(input())
cnt=0
result=0
for _ in range(x):
    y = str(input())
    z = ""
    for i in y:
        if i =='O':
            cnt +=1
        else:
            cnt =0
        result +=cnt
    print(result)
        