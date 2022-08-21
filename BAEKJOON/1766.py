import sys,heapq,collections
input = sys.stdin.readline
N,M = map(int,input().split())
nums = [0 for _ in range(N)]
dic = collections.defaultdict(list)
for _ in range(M):
    a,b = map(int, input().split())
    nums[b-1] += 1
    dic[a-1].append(b-1)
h = []
for i,v in enumerate(nums):
    if not v:
        heapq.heappush(h,i)
while h:
    i = heapq.heappop(h)
    print(i + 1, end = " ")
    for index in dic[i]:
        nums[index] -= 1
        if not nums[index]:
            heapq.heappush(h,(index))

