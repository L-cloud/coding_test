import sys
input = sys.stdin.readline
N, M = map(int,input().split())
memories = list(map(int,input().split()))
costs = list(map(int,input().split()))
dic,min_cost = {},float('inf')
for i in range(N): 
    if M <= memories[i]:
        min_cost = min(min_cost,costs[i])
        continue 
    a = dic.get(costs[i],0)
    tempt = {}
    tempt[costs[i]] = max(a,memories[i])
    for j in list(dic.keys()):
        memory , cost =  dic[j] + memories[i], j + costs[i]
        if M <= memory: 
            min_cost = min(cost, min_cost)
        else :
            a = dic.get(cost,0) 
            tempt[cost] = max(a,memory) 
    dic.update(tempt)
print(min_cost)
