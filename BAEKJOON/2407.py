m,n = map(int,input().split())
n = min(n,m-n)
answer = 1
cnt = n
while cnt:
    answer *= m
    m -= 1
    cnt -= 1
while n:
    answer //= n
    n -= 1
print(answer)