def solution(s:str, skip:str, index:int) -> str:
    abc="abcdefghijklmnopqrstuvwxyz"
    answer = [c for c in s]
    for i in range(0,len(answer)):
        t = index
        c = abc.find(answer[i])
        while t > 0:
            c = (c+1) % 26
            if abc[c] not in skip: t-= 1
        answer[i] = abc[c]
    return "".join(answer)
