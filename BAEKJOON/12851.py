import sys,heapq

start, end = map(int,sys.stdin.readline().split())
visited = {start:0}
h = [(0,start)]
time, cnt = float('inf'),0
def check(node, t):
    if node in visited:
        if visited[node] == t + 1:
            heapq.heappush(h, (t+1, node))
    else:
        visited[node] = t + 1
        heapq.heappush(h,(t+1,node))
while h:
    t, node = heapq.heappop(h)

    if node == end:
        time = t
        cnt += 1
        continue
    if time < t: 
        continue
    if node + 1 < end + 1:
        check(node + 1,t)
    if node *2 < end * 2 + 1:
        check(node * 2, t)
    if  -1< node -1 :
        check(node -1 , t)
print(time)
print(cnt)