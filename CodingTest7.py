##Stack and Queue
from collections import deque

stack = []
stack.append(1)
stack.append(3)
stack.append(5)
print(stack)
stack.pop()
print(stack)
print("------------------")
queue = deque()
queue.append(3)
queue.append(5)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
