import collections
from typing import List
import bisect
def solution(operations :List[str]) -> List[str]:
    answer = collections.deque()
    for command in operations:
        if command[0] == 'I' :
            command, num = command.split()
            bisect.insort_left(answer, int(num))
        elif command == 'D 1' and answer:
            answer.pop()
        elif command == 'D -1' and answer:
            answer.popleft()
    if answer:
        return [answer[-1], answer[0]]
    return [0,0]