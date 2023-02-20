from typing import List
import copy
def solution(triangle:List[int]) -> int:
    for i in range(len(triangle) - 1):
        t = [j for j in triangle[i + 1]]
        for j in range(len(triangle[i])):
            t[j] = max(t[j], triangle[i+1][j] + triangle[i][j])
            if j < len(triangle) - 1:
                t[j + 1] = max(t[j+1],triangle[i + 1][j+1] + triangle[i][j])
        triangle[i + 1] = t 
    return max(triangle[-1])
