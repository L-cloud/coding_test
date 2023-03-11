import sys, copy
from collections import defaultdict
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N,M = map(int, input().split())

def dfs(v:set,start:int,x:int,min_value:int) -> None:
    for node in graph[x]:
        if node not in v:
            v.add(node)
            matrix[start].update({node:min(min_value, graph[x][node])})
            dfs(v,start, node, min(min_value, graph[x][node]))

graph = defaultdict(dict)
for _ in range(N-1):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].update({b:c})
    graph[b].update({a:c})

matrix = copy.deepcopy(graph)
[dfs({i},i,i,float('inf')) for i in range(1,N+1)]
for _ in range(M):
    k,v = map(int, input().split())
    print(sum([1 for key,value in matrix[v].items() if value>= k and key != v]))


'''
필요한 인자

1. 최솟값 인자 -> 이건 bfs 할 때 넘겨야함 depth별로 넘기는 것 x
cache의 효과가 너무 적음. 분명 한 번 탐색할 때 다른 모든 것들 update 가능함 

0~N-1 까지 자기가 연결 된 것만 체크하면 되는거아님? 그렇게 해서 상대방 update해줌 -> 반례가 있지 않을까 

1. 자기랑 연결된 노드 == 노드 간의 최솟 값임. 루프 다 돌고 최솟 값을 구함(x)

이제 이 x 를 가지고 자신과 연결한 녀석들을 update해주면 됨 



'''


# 다수로 연결된 것을 어떻게 하지??
# 그냥 처음부터 다시 생각해보자
