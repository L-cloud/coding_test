from typing import List
def solution(n:int, k:int)->List[int]:
    l = n
    n,answer,v = [i for i in range(1,n+1)], [], 0
    while len(answer) != l:
        v = sol(n,k,v,answer)
    return answer

def sol(n:List[int], k:int, v:int, answer:List[int])->int:
    for i in n:
        v += fac(len(n) - 1)
        if k < v:
            v = v - fac(len(n) - 1)
            answer.append(i)
            n.remove(i)
            return v
        elif k == v:
            answer.append(i)
            n.remove(i)
            answer.extend(n[::-1])
            return k
            
def fac(n:int) -> int:
    i = 1
    while n :
        i *= n
        n -= 1
    return i
