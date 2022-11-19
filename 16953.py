import sys
input = sys.stdin.readline

x, y = map(int, input().split())

cnt = 1


while True:
    if y >= x:
        if x == y:
            break
        elif y % 10 == 1:
            cnt += 1
            y //= 10
        elif y % 2 == 0:
            cnt += 1
            y //= 2
    elif y < x or (y % 10 != 1 and y % 2 != 0):
        cnt = -1
        break
print(cnt)
