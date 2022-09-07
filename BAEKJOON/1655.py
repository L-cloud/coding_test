
import sys,heapq
input = sys.stdin.readline
N = int(input())
l_h, r_h = [],[]
mid = int(input())
print(mid)
for i in range(1,N):
    num = int(input())
    if mid <=num:
        heapq.heappush(r_h,num)
    else:
        heapq.heappush(l_h, -num)
    if  i // 2 < len(l_h): # 중간값 보다 큼
        heapq.heappush(r_h,mid)
        mid = -heapq.heappop(l_h)
    elif len(l_h) < i // 2: # 중간값 보다 작음
        heapq.heappush(l_h,-mid)
        mid = heapq.heappop(r_h)
    print(mid)



