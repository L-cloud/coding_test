import sys, collections
from typing import List
input = sys.stdin.readline
def dfs(m:int,node:int,item:int,distance:List[int]) -> int:
    for road,cost in roads[node]:
        if cost <= m and distance[road] < m-cost:
            if distance[road] == -1: # 이전에 방문 x
                distance[road] = m-cost
                item += dfs(m-cost,road, items[road],distance) # item을 더해준다
            else:
                distance[road] = m-cost
                item += dfs(m-cost,road,0,distance) # 아이템을 더하지 않고 방문
    return item
n,m,r = map(int, input().split())
items = list(map(int,input().split()))
roads = collections.defaultdict(list)
max_item = 0
for _ in range(r):
    a,b,l = map(int,input().split())
    roads[a-1].append([b-1,l])
    roads[b-1].append([a-1,l])
for i in range(n):
    distance = [-1 for  _ in range(n)]
    distance[i] = 16
    max_item = max(dfs(m,i,items[i],distance),max_item)

print(max_item)

