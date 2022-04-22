from collections import deque
import sys
n = int(input())
que = deque()

for i in range(n):
    data_input = sys.stdin.readline().split()

    if(data_input[0] == 'push'):
        que.append(int(data_input[1]))
    elif(data_input[0] == 'pop'):
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif(data_input[0] == 'empty'):
        if que:
            print(0)
        else:
            print(1)
    elif(data_input[0] == 'size'):
        print(len(que))
    elif(data_input[0] == 'front'):
        if que:
            print(data_input[0])
        else:
            print(-1)
    elif(data_input[0] == 'back'):
        if que:
            print(data_input[-1])
        else:
            print(-1)
