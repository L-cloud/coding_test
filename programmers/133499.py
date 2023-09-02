from typing import List
def solution(babbling:List[str]) -> int:
    l = {"aya", "ye", "woo", "ma"}
    cnt = 0
    for bab in babbling:
        index = 0
        prev = ""
        while index < len(bab):
            if bab[index : index + 3] in l and prev != bab[index:index + 3]:
                prev = bab[index:index + 3]
                index += 3
                continue
            if bab[index : index + 2] in l and prev != bab[index : index + 2]:
                prev = bab[index:index + 2]
                index += 2
                continue
            break
        if index >= len(bab): cnt+=1
    return cnt
