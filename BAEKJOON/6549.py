import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1:
        break
    values = 0
    stack = []
    nums = nums[1:]
    for i,v in enumerate(nums):
        while stack and  v < stack[-1][0] :
            value, index = stack.pop()
            if not stack:
                values = max(values,value * i)
            else:
                values = max(value * (i - stack[-1][1] - 1),values)
        stack.append([v,i])
    while stack:
        value, index = stack.pop()
        if not stack:
            values = max(values, value * len(nums))
        else:
            values = max(value * (len(nums) - stack[-1][1] - 1),values)
    print(values)