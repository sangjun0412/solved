import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)


# for _ in range(n):
#     number = int(input())
#     if list1 == [] and number == 0:
#         print(number)
#     elif number != 0:
#         list1.append(number)
#     if number == 0 and list1 != []:
#         print(min(list1))
#         list1.remove(min(list1))
# 시간 초과 ~
