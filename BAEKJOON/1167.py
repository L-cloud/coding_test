import collections,sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
t = collections.defaultdict(list)
answer = [0]
for _ in range(N):
    u_i = list(map(int, sys.stdin.readline().split()))
    parent = u_i[0]
    i = 1
    while i < len(u_i) and u_i[i] != - 1:
        child = u_i[i]
        cost = u_i[i+1]
        t[parent].append([child,cost])
        i += 2
def dfs(node,visited): ## 이거 간선이 2개 이상일지도
    if not t[node]: # 끝임
        return 0
    tempt = [0 for _ in range(len(t[node]))]
    for i in range(len(t[node])):
        n, c = t[node][i][0], t[node][i][1]
        if n not in visited:
            visited.add(n)
            n_c = dfs(n,visited) + c
            tempt[i] = n_c
    #print(tempt)
    answer[0] = max(answer[0], sum(sorted(tempt, reverse = True)[0:2]))
    #print("node =",node,"cost =",answer[0])
    return max(tempt)
dfs(1,{1})
print(*answer)

