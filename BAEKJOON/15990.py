
import sys
num_list = []
for _ in range(int(sys.stdin.readline())):
    num_list.append(int(sys.stdin.readline()))

num = max(num_list)
dp = [[0,0,0,0] for _ in range(num + 1)]
dp[1] = [1,1,0,0] #[[1]], [1,0,0]
dp[2] = [1,0,1,0]  #[[2]], [0,1,0]
dp[3] = [3,1,1,1] #[[1,2],[2,1],[3]]

for n in range(4,num + 1):
    three = (dp[n - 3][0] - dp[n - 3][3]) % 1000000009
    two = (dp[n - 2][0] - dp[n - 2][2]) % 1000000009
    one = (dp[n - 1][0] - dp[n - 1][1]) % 1000000009
    dp[n] = [(one + two + three) % 1000000009, one, two, three]

for num in (num_list):
    print(dp[num][0])