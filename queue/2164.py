from collections import deque
n = int(input())
stack = deque([i+1 for i in range(n)])

while len(stack)>1:
    stack.popleft()
    stack.rotate(-1)

print(stack[0])
