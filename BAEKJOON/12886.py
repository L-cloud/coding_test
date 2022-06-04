import sys
sys.setrecursionlimit(10**9)
num = list(map(int,input().split()))
visited = set()
def dfs(n1:int,n2:int,n3:int) -> bool:
    if (n1,n2,n3) in visited: # 이미 방문
        return False
    visited.add((n1,n2,n3))
    t1,t2,t3 = False,False,False
    if n1 == n2 == n3:
        return True
    else:
        if n1<n2:
            t1 = dfs(n1*2,n2-n1,n3)
        elif n2 < n1:
            t1 = dfs(n1-n2,n2*2,n3)
        if n2 <n3 and not t1:
            t2 = dfs(n1, n2*2,n3-n2)
        elif n3<n2 and not t1:
            t2 = dfs(n1,n2-n3,n3*2)
        if n1 < n3 and (not t1 or not t2):
            t3 = dfs(n1*2,n2,n3-n1)
        elif n3 < n1 and (not t1 or not t2):
            t3 = dfs(n1-n3,n2,n3*2)
    if t1 or t2 or t3:
        return True
if dfs(num[0],num[1],num[2]):
    print(1)
else:
    print(0)
