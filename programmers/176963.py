from typing import List
def solution(name:List[str], yearning:List[int], photo:List[List[str]]) -> List[int]:
    dic = {name[i]:yearning[i] for i in range(0,len(name))}
    return [ sum(dic[photo] if photo in dic else 0 for photo in photo[i]) for i in range(len(photo))]
