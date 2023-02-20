from typing import List
from collections import Counter,deque
def solution(k : int, tangerine : List[int]):
    cnt, answer = deque(Counter(tangerine).most_common()), 0
    while k > 0:
        key, value = cnt.popleft()
        k -= value
        answer += 1
    return answer
