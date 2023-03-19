from typing import List, Dict
from collections import defaultdict
def solution(enroll:List[str], referral:List[str], seller:List[str], amount:List[int]):
    parent_tree = {c:p for p,c in zip(referral, enroll)}
    hierarchy = {c : 0 for c,p in parent_tree.items() if p == "-"}
    total = defaultdict(int)
    
    def find(name:str) -> int:
        if hierarchy.get(name, None) is not None: return hierarchy[name] 
        hierarchy[name] = find(parent_tree[name]) + 1
        return hierarchy[name]
    
    [find(name) for name in enroll]
    for name, cnt in zip(seller, amount):
        parent = parent_tree[name]
        cnt *= 100
        pee = cnt // 10
        total[name] += cnt - pee
        while pee and parent != '-':
            m = pee - pee // 10
            total[parent] += m
            pee //= 10
            parent = parent_tree[parent]
    return [total[name] for name in enroll]
    
    
