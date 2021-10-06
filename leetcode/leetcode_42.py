from typing import List
class Solution:
    def trap(self, height: List[int]) -> int: # my version
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
            if stack == []:
                max_value = h
            stack.append(h)
        return water


    def trap(self, height:List[int]) -> int: # using two pointer
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left <right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # move to high
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

    def trap(self, height:List[int]) -> int: #using stack
        stack = []
        volume = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)
        return volume

