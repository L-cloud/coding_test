import sys
input = sys.stdin.readline
n, m = map(int,input().split())
coupons = list(list(map(int,input().split())) for _ in range(m))
coupons.sort(key = lambda x:x[1])
yen = 0
for i,j in coupons:
	if m <= 1:
		print(yen)
		break
	if i < n:
		yen += (n-i)
	m -= 1

