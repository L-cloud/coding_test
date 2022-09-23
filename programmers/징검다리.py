from typing import List
def solution(stones:List[int], k:int):
    times= max(stones) * len(stones)
    left, right = 0, times
    while left <= right:
        mid = left + (right -left) // 2
        chance = k
        for stone in stones:
            if stone < mid:
                chance -= 1
            else:
                chance = k
            if not chance:
                break
        if not chance:
            right = mid -1
        else:
            left = mid + 1
    return (left + right) // 2 
