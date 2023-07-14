import sys
input = sys.stdin.readline
N = int(input())
cnt = {i:1 for i in range(1,10)}
cnt[0] = 0
for i in range(2,N+1):
    tempt = {}
    for i in cnt:
        # 0일 경우 -1 안됨 9일 경우 +1 안됨
        if not i:
            tempt[i] = cnt[i+1]
        elif i == 9:
            tempt[i] = cnt[i - 1]
        else:
            tempt[i] = cnt[i+1] + cnt[i-1]
    cnt = tempt
print(sum([cnt[i] for i in cnt]) % 1000000000)
