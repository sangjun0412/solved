import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [] * m

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[0] * (m) for _ in range(n)]


def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            dfs(nx, ny)


for i in range(m):
    if graph[0][i] == 0:
        dfs(0, i)


if 2 in graph[-1]:
    print("YES")
else:
    print("NO")
