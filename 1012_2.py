import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())


def search(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return
    if graph[x][y] == 0:
        return
    graph[x][y] = 0
    search(x-1, y)
    search(x, y-1)
    search(x+1, y)
    search(x, y+1)


for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                search(i, j)
                cnt += 1
    print(cnt)
