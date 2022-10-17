from typing import List
def solution(numbers:List[int]) -> List[int]:
    return [check(num) for num in numbers]

def check(a:int) -> bool:
    if a < 2:
        return a + 1
    a = list(map(str,bin(a)[:1:-1]))
    for i,v in enumerate(a):
        if v == '0': # 가장 작은 0 켜기
            a[i] = '1'
            break
    if i == len(a) -1: # 없음 
        a.append('1')
        a = a[::-1]
        for i,v in enumerate(a[1:],1):
            if v == '1':
                a[i] = '0'
                return int(''.join(a),2)
    for j in range(i-1,-1,-1): # 0켠 곳 보다 더 낮은 곳에서 1 끄기 
        if a[j] == '1':
            a[j] = '0'
            break
    
    return int(''.join(a[::-1]),2)
    
