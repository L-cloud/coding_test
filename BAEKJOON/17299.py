import heapq
import sys
import collections
num = [-1 for i in range(int(sys.stdin.readline()))]
h = []
sequence_ = list(map(int, (sys.stdin.readline().split())))
cnt = collections.Counter(sequence_)

for i,v in enumerate(sequence_):
    while h:
        index, value = heapq.heappop(h)[1]
        if cnt[value] < cnt[v]:
            num[index] = v
            continue
        else:
            heapq.heappush(h,(cnt[value],(index,value)))
            break
    heapq.heappush(h,(cnt[v],(i,v)))
print(" ".join(map(str,num)))
    