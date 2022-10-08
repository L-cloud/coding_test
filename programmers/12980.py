# K 칸 점프, (현재까지 온 거리) * 2
# K 칸 점프 -> K 만큼 건전지 사용량  # 앞으로만 가능
# 점프 이동 최소화해서 N으로 가기
from heapq import heappop, heappush
def solution(n:int) -> int:
    ans = 0
    while n :
        if n % 2:
            n //= 2
            ans += 1
        else:
            n //= 2
    return ans
