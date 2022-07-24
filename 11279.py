import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []


for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        try:
            print(heapq.heappop(heap)*(-1))
        except:
            print(0)
