from typing import List
def solution(n:int, info:List[int]):
    answer,max_score = [],0
    def dfs(n:int, info:List[int], tempt:List[int], index:int):
        if index == 11 or not n:
            nonlocal answer, max_score
            tempt[-1] += n
            lion_score,apeach_score = 0,0
            for i in range(11):
                if info[i] < tempt[i]:
                    lion_score += 10 -i
                elif info[i]:
                    apeach_score += 10 -i
            diff = lion_score - apeach_score
            if 0 < diff  and max_score <= diff:
                answer = compare(tempt,answer)[:] if diff == max_score else tempt[:]
                max_score = diff
            tempt[-1] = 0
            return
        if info[index]<n:
            tempt[index] = info[index] + 1
            dfs(n-tempt[index],info,tempt,index + 1)
            tempt[index] = 0
        dfs(n,info,tempt,index+1)
    
    dfs(n,info,[0]*11,0)
    
    return answer if answer else [-1]

def compare(a:List[int],b:List[int]):
    if a and b:
        for i in range(10,-1,-1):
            if b[i] < a[i]:
                return a
            elif a[i]<b[i]:
                return b
        return a # 둘이 같음
    return a

