from typing import List
def solution(numbers:List[int]) -> List[int]:
    answer = []
    for number in numbers:
        s = bin(number)[2:]
        k = findk(len(s))
        s = "0" + "0" *  (k - len(s)) + s # 인덱스 1번부터 하기 위해서
        s = [i for i in s]
        # 루트는 무조건 1 
        answer.append(check(s))
        
    return answer

def findk (n:int) -> int:
    k = 0
    while (1<<k) -1 < n : k += 1
    return (1 << k) -1

def check(s:List[str]) -> int: # 되는지 안 되는지 확인
    # lv 별로 확인하면 됨 index + lv *2 이거임 
    lv = 1
    while lv * 2 < len(s):
        index = 0
        for i in range(lv, len(s),lv*2):
            index += 1
            if s[i] == '0': continue 
            if index % 2 and  s[i + lv] == '0' : return 0 
            if not index % 2 and s[i -lv] == '0': return 0
        lv *= 2
    return 1
