def solution(n:int, q:List[List[int]], ans:List[int]):
    answer = 0
    for candi in itertools.combinations(range(1,n+1), 5):
        for index, user_try in enumerate(q):
            if count(candi, set(user_try)) != ans[index]:
                break
        else:
            answer += 1
    return answer
        
def count(candi:Tuple[int], user_try:Set[int]) -> int:
    return sum([c in user_try for c in candi])
