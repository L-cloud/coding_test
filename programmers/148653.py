def solution(storey:int) -> int:
    s = str(storey)
    s = [int(i) for i in s[::-1]]
    answer = 0
    for i,v in enumerate(s):
        if v < 5:
            answer += v
        elif v == 5:
            if i != len(s) - 1: # 마지막 아님
                if 4 < s[i+1]:
                    s[i +1] += 1
            answer += 5    
        else: # 아 5일 때 고민을 해줘야하네
            if i != len(s) - 1: # 마지막 아님
                s[i+1] += 1
                answer += (10 - v)
            else:
                answer += (10 - v) + 1
    return answer

