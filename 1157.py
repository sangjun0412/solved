def solve():
    s = input()
    s = s.upper()
    hist = {}

    for c in s:
        if c in hist.keys():
            hist[c] += 1
        else:
            hist[c] = 1

    compare=0

    for b in hist.keys():
        compare = max(compare, hist[b])
    cnt = 0
    for c in hist.keys():
        if hist[c]== compare:
            cnt +=1
            result=c
    if cnt != 1:
        print("?")
    else:
        print(result)
solve()