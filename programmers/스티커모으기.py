from typing import List
def solution(stickers:List[int])->int:
    if len(stickers) < 4:
        return max(stickers)
    dp1 = stickers[1:]
    dp2 = stickers[:len(stickers) - 1]
    for i in range(len(dp1)):
        if 1 < i :
            dp1[i] = max(dp1[i] + dp1[i-2], dp1[i-1])
            dp2[i] = max(dp2[i] + dp2[i-2], dp2[i -1])
        elif i ==  1:
            dp1[i] = max(dp1[i],dp1[i-1])
            dp2[i] = max(dp2[i],dp2[i-1])
    return max(max(dp1),max(dp2))
