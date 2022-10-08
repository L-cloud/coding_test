# O(n) 안으로 해야함
from typing import List
def solution(n:int, left:int, right:int) -> List[int]:
    return  [max(i//n,i%n) + 1 for i in range(left,right + 1)]


