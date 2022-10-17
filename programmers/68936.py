from typing import List
def solution(arr:List[List[int]]):
    answer = [0,0]
    dfs(0,len(arr),0,len(arr),arr,answer)
    return answer

def dfs(lo:int,hi:int,left:int,right:int, arr:List[List[int]],answer:List[int]) -> None:
    if right - left == 1: # 더 못 나눔
        answer[arr[lo][left]] += 1
        return
    prev = arr[lo][left]
    for i in range(lo,hi):
            for j in range(left,right):
                if prev != arr[i][j]:
                    dfs(lo,(hi+lo)//2, left,(left+right)//2,arr,answer)
                    dfs(lo,(hi+lo)//2, (left+right)//2,right,arr,answer)
                    dfs((hi+lo)//2, hi,left,(left+right)//2,arr,answer)
                    dfs((hi+lo)//2,hi, (left+right)//2,right,arr,answer)
                    return
    answer[arr[lo][left]] += 1
    return
