from typing import List
import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
opers = list(map(int,input().split()))
min_value, max_value = float('inf'),-float('inf')

def mul(a:int,b:int)->int:
    return a*b
def add(a:int,b:int)->int:
    return a+b
def divide(a:int,b:int) ->int:
    if a < 0:
        return -((-a)//b)
    else:
        return a //b
def minus(a:int,b:int)->int:
    return a - b

func = {0:add,1:minus,2:mul,3:divide}
def dfs(nums:List[int],opers:List[int],cnt:int,value:int,func:dict)->None:
    if cnt == len(nums):
        global min_value, max_value
        min_value = min(min_value,value)
        max_value = max(max_value,value)
        return
    for i in range(4):
        if opers[i]:
            opers[i] -=1
            t_value = func[i](value,nums[cnt])
            dfs(nums,opers,cnt+1,t_value,func)
            opers[i] += 1
dfs(nums,opers,1,nums[0],func)
print(max_value)
print(min_value)
