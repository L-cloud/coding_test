import sys,collections
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
cnt = collections.Counter(nums)
for index,value in enumerate(sorted(cnt.keys(), reverse= True), 1):
    cnt[value] = len(cnt) - index
print(*[str(cnt[i]) for i in nums])
