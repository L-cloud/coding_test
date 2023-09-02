def solution(s:str) -> int:
    index = 0
    cnt = 0
    while index < len(s):
        i = s[index]
        sc = 0
        dc = 0
        for p,c in enumerate(s[index:]):
            if c == i : sc += 1
            else : dc += 1
            if sc == dc:
                index += p+1
                cnt += 1
                break
        else:
            cnt += 1
            break
    return cnt
