from typing import List
def solution(A:List[int], B:List[int]) -> int:
    A.sort()
    B.sort()
    i,j = 0,0
    answer = 0
    while i < len(A) and j < len(A):
        if A[i] < B[j]:
            i += 1
            j += 1
            answer += 1
        else :
            j+=1
    return answer
