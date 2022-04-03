import sys,collections

N = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
graph = collections.defaultdict(list)
visited = [False for _ in range(N)]
for _ in range(edge):
  a, b = map(int, sys.stdin.readline().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

q = collections.deque([0])
visited[0] = True
virus = -1
while q:
  for _ in range(len(q)):
    computer = q.pop()
    virus += 1
    for node in graph[computer]:
      if not visited[node]:
        visited[node] = True
        q.appendleft(node)

print(virus)
        
