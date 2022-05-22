import sys, itertools
N, K = map(int,sys.stdin.readline().split())
strings = [set(sys.stdin.readline().rstrip()) - {'a','n','t','c','i'} for _ in range(N)]
if K < 5 :
    print(0)
    exit()
candi = set()
for s in strings:
    for i in s:
        candi.add(i)

max_cnt = 0
if len(candi) < K - 5:
    for s in strings:
        if s & candi == s:
            max_cnt += 1
    print(max_cnt)
else:
    for i in itertools.combinations(candi,K - 5):
        a = set(i)
        cnt = 0
        for s in strings:
            if s & a == s: # 교집함
                cnt += 1
        max_cnt = max(max_cnt,cnt)
    print(max_cnt)