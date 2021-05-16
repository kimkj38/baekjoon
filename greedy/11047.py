import sys
from collections import deque

cmd = sys.stdin.readline().split()
N = int(cmd[0])
K = int(cmd[1])
moneylist = deque([])
totalcount = 0

for i in range(N):
    money = int(sys.stdin.readline())
    moneylist.append(money)

while K>0:
    count = K//moneylist[-1]
    totalcount += count
    K = K%moneylist[-1]
    moneylist.pop()

print(totalcount)
