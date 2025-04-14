from typing import List
def solution(cards1 : List[str], cards2 : List[str], goal : List[str]) -> str:
    c1_index, c2_index = [], []
    for g in goal:
        if g in cards1:
            index = cards1.index(g)
            if c1_index and c1_index[-1] + 1 != index:
                return "No"
            c1_index.append(index)
        elif g in cards2:
            index = cards2.index(g)
            if c2_index and c2_index[-1] + 1 != index:
                return "No"
            c2_index.append(index)
        
    return "Yes"
