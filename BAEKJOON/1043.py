
import sys,collections
def q(node:int):
    h = collections.deque([node])
    while h:
        n = h.pop()
        while exaggeration[n]: # 굳이 for문 돌지말고 그냥 여기서 pop() 해서 없애는게 나음
            i  = exaggeration[n].pop()
            for people in parties[i][1:]:
                if people not in true_people:
                    h.appendleft(people) 
                    p[i] = False
        true_people.add(n)
N,M = map(int, sys.stdin.readline().split())
true_people = list(map(int, sys.stdin.readline().split())) # 0일 가능성 있음
true_people = set(true_people[1:]) if len(true_people) > 1 else []
parties = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
exaggeration = collections.defaultdict(list)  # 과장 모르는 사람이 들어있는 인덱스
p = [False for _ in range(M)]
for index,party in enumerate(parties):
    f = True
    for people in party[1:]:
        if people in true_people:
            f = False
            break
    if f:
        for people in party[1:]:
            exaggeration[people].append(index)
        p[index] = True
    else:
        for people in party[1:]:
            if exaggeration[people]:
                q(people)
            else:
                true_people.add(people)
print(sum(p))