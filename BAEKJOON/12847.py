import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
s,c =sum(arr[:m]), sum(arr[:m])
f,e = 0, m
while e < n:
	c -= arr[f]
	c += arr[e]
	s = max(s,c)
	f += 1
	e += 1
print(s)
