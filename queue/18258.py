from collections import deque
import sys
n = int(sys.stdin.readline())
stack = deque([])

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.popleft())
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif cmd[0] == "back":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
