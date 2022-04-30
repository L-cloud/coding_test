def solution(stones, k):
    start , end = 0 , max(stones)
    mid = (start + end) // 2
    big = False # 건너버린 인원이 더 큰가
    while start <= end:
        tempt = [i - mid for i in stones]
        chance = k
        big = False
        for s in tempt:
            if s < 0:
                chance -= 1
            else:
                chance = k
            if chance <= 0:
                big = True
                break
        if big:
            end = mid - 1
        else: # 실제 건널 수 있는 것보다 적게 건넘
            start = mid + 1
        mid = (start + end) // 2          
    return mid
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))