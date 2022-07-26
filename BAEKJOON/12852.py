import sys,heapq
input = sys.stdin.readline
N = int(input())
visited = set([N])
h = [(0,[N])]
while True:
    cnt, node = heapq.heappop(h)
    if node[-1] == 1:
        print(cnt)
        print(*node)
        break
    if node[-1] % 3 == 0 and node[-1] // 3 not in visited:
        heapq.heappush(h,(cnt+1, node + [node[-1]//3]))
        visited.add(node[-1]//3)
    if node[-1] % 2 == 0 and node[-1] // 2 not in visited:
        heapq.heappush(h, (cnt + 1, node + [node[-1] // 2]))
        visited.add(node[-1] // 2)
    if node[-1] > 1 and node[-1] -1 not in visited:
        heapq.heappush(h,(cnt + 1 , node + [node[-1] - 1]))
        visited.add(node[-1] -1)
