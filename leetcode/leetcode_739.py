class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack,output = [],[0] * len(temperatures)
        for index,temper in enumerate(temperatures):
            while stack and stack[-1][1]< temper:
                i,v = stack.pop()
                output[i] = index - i
            stack.append([index,temper])
        return output
