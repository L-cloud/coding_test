import sys
import itertools


def team_sum(a_team:tuple, b_team:set) -> int:
    a_sum, b_sum = 0,0
    for i,v1 in enumerate(a_team):
        for j,v2 in enumerate(a_team):
            if i == j:
                continue
            a_sum += team[v1-1][v2-1]
    
    for i,v1 in enumerate(b_team):
        for j,v2 in enumerate(b_team):
            if i == j:
                continue
            b_sum += team[v1-1][v2-1]
    return abs(a_sum - b_sum)

people = int(sys.stdin.readline())
team = []
min_sum = float('inf')
for _ in range(people):
    team.append(list(map(int, sys.stdin.readline().split())))

for a_team in (itertools.combinations(range(1,people + 1), people//2)):
    p = set([i for i in range(1, people + 1)])
    b_team = p - set(a_team)
    min_sum = min(team_sum(a_team,b_team),min_sum)
print(min_sum)
