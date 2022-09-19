
import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1:
        break
    values = [0] * (len(nums) - 1)
    stack = []
    nums = nums[1:]
    for i,v in enumerate(nums):
        if not stack or stack[-1][0] <= v:
            stack.append([v,i])
            continue
        max_index = stack[-1][1]
        while stack and  v < stack[-1][0]:
            value, index = stack.pop()
            values[index] = value * (max_index -index + 1)
        stack.append([v,i])
    if stack:
        max_index = stack[-1][1]
        while stack:
            value,index = stack.pop()
            values[index] = value*(max_index-index + 1) 
    stack = []
    for i,v in enumerate(reversed(nums)):
        if not stack or stack[-1][0] <= v:
            stack.append([v,i])
            continue
        max_index = stack[-1][1]
        while stack and  v < stack[-1][0]:
            value, index = stack.pop()
            values[len(nums)-index -1] += value * (max_index -index)
        stack.append([v,i])
    if stack:
        max_index = stack[-1][1]
        while stack:
            value,index = stack.pop()
            values[len(nums)-index -1] += value*(max_index-index) 
    print(max(values))
                     
