from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        water,max_value,stack= 0,0,[]
        for h in height:
            if stack and stack[-1] < h:
                if h < max_value:
                    for i in range(-1, -len(stack), -1):
                        if stack[i] < h:
                            water += h - stack[i]
                            stack[i] = h
                        else:
                            break
                else: # h >= max_value
                    while stack:
                        water += max_value - stack.pop()
                    max_value = h
                stack.append(h)
            else: # stack == [] or stack[-1] >= h
                if stack == []:
                    max_value = h
                stack.append(h)
        return water


a = Solution()
print(a.trap([4,2,0,3,2,5]))