from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
house = []
chicken = []
distance = 9999
for i in range(N):
    graph.append(list(map(int, input().split())))

# 0은 빈칸, 1은 집, 2는 치킨집

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            house.append([i + 1, j])
        elif graph[i][j] == 2:
            chicken.append([i + 1, j])

cand = []

for comb in list(combinations(chicken, M)):
    answer = 0
    for h in house:
        x1, y1 = h
        dist = int(1e9)
        for c in comb:
            x2, y2 = c
            dist = min(dist, abs(x1-x2) + abs(y1-y2))
        answer += dist
    cand.append(answer)
print(min(cand))
