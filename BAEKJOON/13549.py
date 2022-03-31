import sys, heapq

me, brother = map(int, sys.stdin.readline().split())
visited = set([me])
h = [(0,me)] # time, location
while h:
    time, location = heapq.heappop(h)
    if location == brother:
        print(time)
        break
    if location * 2 <= brother + 1 and location * 2 not in visited:
        heapq.heappush(h, (time, location*2))
        visited.add(location * 2)
    if 0<= location -1 and location -2 not in  visited:
        heapq.heappush(h,(time +1, location-1))
        visited.add(location -1)
    if location + 1 <= brother and  location + 1 not in visited:
        heapq.heappush(h,(time +1, location+1))
        visited.add(location + 1)

