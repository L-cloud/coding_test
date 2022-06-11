import sys,collections
a,b = map(int, sys.stdin.readline().split())
q,tri = collections.deque([a]),0

while q:
    for _ in range(len(q)):
        node = q.pop()
        if node == b:
            print(tri + 1)
            exit()
        else:
            if node*2 <= b:
                q.appendleft(node*2)
            if int(str(node) +'1') <= b:
                q.appendleft(int(str(node) +'1'))
    tri += 1
print(-1)