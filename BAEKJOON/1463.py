import sys
import heapq
num = int(sys.stdin.readline())
visited = set()
h = []
current = heapq.heappush(h, (0,num))
while True:
    cnt, num = heapq.heappop(h)
    if num == 1:
        print(cnt)
        break
    if num % 3 == 0:
        if num // 3 not in visited:
            visited.add(num//3)
            heapq.heappush(h,(cnt + 1, num //3))
    if num % 2 == 0:
        if num //2 not in visited:
            visited.add(num // 2)
            heapq.heappush(h, (cnt + 1, num//2))
    if (num -1) % 3 == 0 or (num-1)% 2 ==0:
        if num - 1 not in visited:
            visited.add(num -1)
            heapq.heappush(h, (cnt + 1, num -1))
    