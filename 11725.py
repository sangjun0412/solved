import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

visited = [0] * (n + 1)


def dfs(node):
    for i in graph[node]:
        if visited[i] == 0 and i != 1:
            visited[i] = node
            dfs(i)


dfs(1)

for i in range(2, n + 1):
    print(visited[i])
