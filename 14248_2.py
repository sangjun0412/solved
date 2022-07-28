import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
start = int(input())
visited = [0] * n
cnt = 1


def bfs(x):
    global cnt
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        for nx in (x + graph[x], x - graph[x]):
            if 0 <= nx < n and visited[nx] == 0:
                visited[nx] = 1
                cnt += 1
                q.append(nx)


bfs(start - 1)
print(cnt)
