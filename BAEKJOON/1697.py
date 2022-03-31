import sys
import collections
me, brother = map(int, sys.stdin.readline().split())
time = -1
stack = collections.deque([me])
visited = set([me])
while True: # 공간복잡도 3n이 되어버리네
    time += 1
    for _ in range(len(stack)):
        node = stack.pop()
        if node == brother:
            print(time)
            exit()
        if 0 <= node - 1 and node - 1 not in visited:
            stack.appendleft(node -1)
            visited.add(node -1)
        if node + 1 <= brother and node + 1 not in visited:
            visited.add(node + 1)
            stack.appendleft(node + 1)
        if node * 2 <= brother + 1 and node * 2 not in visited: # 아 
            visited.add(node * 2)
            stack.appendleft(node * 2)

#3 43
# 3 -> 6 -> 12 -> 11 -> 22 -> 44 -> 43
# 증가해버리고 빼면 되는 녀석들이 있음... 아... 
# 역도 잘 생각해야한다. 바보
