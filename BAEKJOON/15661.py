import sys
sys.setrecursionlimit(100000)
def dfs(team:int, team1_set:set, start:int): # 몇 대 몇 으로 나눌지
    if len(team1_set) == team: # 나눠짐
        t1, t2 = 0,0
        team2_set = set(range(N)) - team1_set
        for i in team1_set:
            for j in team1_set:
                t1 += people[i][j]
        for i in team2_set:
            for j in team2_set:
                t2 += people[i][j]
        output = min(output, abs(t1-t2))
        return
    for i in range(start, N): # 문제가 1,2 하고 난 다음에 2,1도 함 그래서 time out
        team1_set.add(i)
        dfs(team, team1_set, i+1)
        team1_set.remove(i)

N = int(sys.stdin.readline())
output = float('inf')
people = []
for _ in range(N):
    people.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,N):
    if N < i * 2:
        break
    dfs(i,set(),0)

print(output[0])
