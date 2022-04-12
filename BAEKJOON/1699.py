# import sys
# import heapq
# N = int(sys.stdin.readline())
# multiple,multi = [0 for _ in range(N + 1)], 1
# cnt = 0
# while multi**2 <= N:
#     multiple[multi] = multi**2
#     multi += 1
# multiple = multiple[1:multi]
# visited = [False for _ in range(N + 1)]
# h = []
# for i in multiple:
#     heapq.heappush(h,(1,-i))
# while True:
#     cnt, num = heapq.heappop(h)
#     if -num == N:
#         print(cnt)
#         exit()
#     for n in multiple:
#         if -(num - n) <= N: 
#             if not visited[-(num - n)]:
#                 heapq.heappush(h,(cnt+1,num-n)) 
#                 visited[-(num-n)] = True

n = int(input())
 
dp = [i for i in range (n+1)]
 
for i in range(1, n+1):
    for j in range(1, i):
        if (j * j) > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
 
print(dp[n])