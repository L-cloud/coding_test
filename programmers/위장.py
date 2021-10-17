import collections
from typing import List
def solution(clothes: List[str]) -> int:
    dic = collections.defaultdict(int)
    answer = 1
    for clothe, kind in clothes:
        dic[kind] += 1
    for key,value in dic.items():
        answer *= (value + 1)
    return answer - 1
