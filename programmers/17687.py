from typing import List
def solution(n:int, t:int, m:int, p:int) -> str:
    # 진법n, 미리 구할 숫자의 갯수 t, 참가인원 m, 튜브 순서p
    answer = []
    number,order = 0, 1 # 숫자, 순서
    while True:
        for i in make_num(number,n):
            if order == p:
                answer.append(i)
                p += m
                if len(answer) == t:
                    return ''.join(answer)
            order += 1
        number += 1
def make_num(num:int,z:int) -> List[str]:
    s = []
    dic = {10:'A',11:'B',12:'C',13:'D', 14:'E',15:'F'}
    while num:
        d = num % z 
        if d in dic:
            s.append(dic[d])
        else:
            s.append(str(d))
        num //=z
    return reversed(s) if s else  ['0']
        

# 진법n, 미리 구할 숫자 t개, 게임 참가 인원 m, 튜브의 순서 p
# n * t = 1600... 

