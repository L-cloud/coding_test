import collections,sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
t = collections.defaultdict(list)
R = [True for _ in range(N+1)]
answer = [0]
for _ in range(N - 1):
    p, v, c = map(int,sys.stdin.readline().split())
    R[v] = False
    t[p].append([v,c]) # 간선, cost
root = R[1:].index(True) + 1
def dfs(node): ## 이거 간선이 2개 이상일지도
    if not t[node]: # 끝임
        return 0
    tempt = [0 for _ in range(len(t[node]))]
    for i in range(len(t[node])):
        n, c = t[node][i][0], t[node][i][1]
        n_c = dfs(n) + c
        tempt[i] = n_c
    #print(tempt)
    answer[0] = max(answer[0], sum(sorted(tempt, reverse = True)[0:2]))
    #print("node =",node,"cost =",answer[0])
    return max(tempt)
dfs(root)
print(*answer)


