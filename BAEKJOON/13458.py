# N개의 시험장 각 시험장 응시자 있음
# i 번 시험장 응시자 수 = Ai 명
# 총 감독관 B명 감시 부감독관 C명 감시
# 감독관 수 최소로
# 그리디 같은데...

import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
ans = N
for i in range(N):
    A[i] -= B
    if 0 < A[i]:
        ans += A[i] // C 
        if A[i] % C :
            ans += 1
print(ans)
