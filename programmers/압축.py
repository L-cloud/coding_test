from typing import List
from collections import deque
def solution(msg:str)->List[int]:
    dic,q = {alpha:index for index, alpha in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ",1)},deque()
    next_num,answer,tempt = 27,[],""
    for m in msg:
        q.append(m)
        tempt += m
        if tempt in dic:
            continue
        else:
            dic[tempt] = next_num
            next_num += 1
            q = deque([m])
            answer.append(dic[tempt[:len(tempt) - 1]])
            tempt = m
    answer.append(dic[tempt])
    return answer

