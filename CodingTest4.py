n = int(input())
x,y = 1,1
n_list = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

type = ['L', 'R', 'U', 'D']

for n in n_list:
    for i in range(4):
        if n == type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x = nx
    y = ny

print(x,y)