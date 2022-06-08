import sys, heapq

N, k = map(int, sys.stdin.readline().split())
jewelry = [list(map(int,sys.stdin.readline().split())) for _ in range(N)] # 무게, 가격
bags = list(int(sys.stdin.readline())for _ in range(k))
jewelry.sort() 
bags.sort()
value,index,h = 0,0,[]
for b in bags:
    while index < N and jewelry[index][0] <= b:
        heapq.heappush(h, -jewelry[index][1])
        index += 1
    if h :
        value -= heapq.heappop(h)
print(value)

