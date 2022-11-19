import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n + 1)


def bfs(x):
    q = deque()
    q.append(x)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                q.append(i)


bfs(x)

if visited[y] == 0:
    print(-1)
else:
    print(visited[y])
