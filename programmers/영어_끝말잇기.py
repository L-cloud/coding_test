from typing import List
def solution(n:int, words:List[str]) -> List[int]:
    answer = [0,0]
    prev,s = None,set()
    for i,v in enumerate(words):
        if (prev and prev[-1] != v[0]) or v in s or len(v) == 1:
            answer = [i % n + 1,i // n + 1]
            break
        s.add(v)
        prev = v
    return answer
