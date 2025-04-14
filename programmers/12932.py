from typing import List
def solution(n:int) -> List[int]:
    return [int(i) for i in str(n)[::-1]]
