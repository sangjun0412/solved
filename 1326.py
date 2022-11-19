import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

list1 = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i].append(list1[i - 1])

visited = [False] * (n + 1)
cnt = 0


def bfs(n):
    q = deque([n])
    visited[n] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[x]:
                bfs()
                visited[x] = True
