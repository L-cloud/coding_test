import sys
input = sys.stdin.readline
def find_index(plane:int) -> bool:
    while dp[possible[plane]]:
        possible[plane] = possible[possible[plane] - 1]
        if not possible[plane]:
            return False
    dp[possible[plane]] = True
    return True
G,P  = int(input()),int(input())
dp = [False] * (G + 1)
possible = {key: key for key in range(G + 1)}
for _ in range(P):
    if not find_index(int(input())):
        print(sum(dp))
        exit()
print(sum(dp))
