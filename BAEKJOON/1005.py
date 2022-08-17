import sys, collections
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,K = map(int, input().split())
    costs  = list(map(int, input().split()))
    graph, cnt = collections.defaultdict(set), [0 for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        cnt[b-1] += 1
        graph[a - 1].add(b - 1)
    W,time  = int(input()) - 1,0
    q = [index for index, value in enumerate(cnt) if not value]
    q.sort(key = lambda x : costs[x],reverse = True)
    flag =  True
    while q and flag:
        tempt = []
        time += costs[q[-1]]
        for x in q:
            costs[x] -= costs[q[-1]] # 최소 값으로 다 빼기
        while q and  not costs[q[-1]] : # cost 0일때 까지
            node = q.pop()
            if node == W:
                print(time)
                flag = False
                break
            for n in graph[node]:
                cnt[n] -= 1
                if not cnt[n]:
                    tempt.append(n)
        q += tempt
        q.sort(key = lambda x : costs[x],reverse=True)

