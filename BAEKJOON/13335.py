import sys
from collections import deque
input = sys.stdin.readline
n,w,l = map(int,input().split())
trucks = deque(map(int, input().split()))
bridge = deque([[1,trucks.popleft()]])
time, bridge_w = 1, bridge[0][1]
while n:
    time += 1
    for i in range(len(bridge)):
        bridge[i][0] += 1
    if w < bridge[-1][0]:
        n -= 1
        bridge_w -= bridge.pop()[1]
    if len(bridge) + 1 <= w and trucks and bridge_w + trucks[0] <= l:
        bridge.appendleft([1, trucks.popleft()])
        bridge_w += bridge[0][1]
print(time)
