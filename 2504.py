from collections import deque

sentence = str(input())
res = 1
stack = []
result = 0

for n, w in enumerate(sentence):
    if w == '(':
        res *= 2
        stack.append(w)
    elif w == '[':
        res *= 3
        stack.append(w)
    elif w == ')':
        if not stack or stack[-1] != '(':
            print(0)
            break
        if sentence[n - 1] == '(':
            result += res
        res = res // 2
        stack.pop()
    elif w == ']':
        if not stack or stack[-1] != '[':
            print(0)
            break
        if sentence[n - 1] == '[':
            result += res
        res = res // 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)