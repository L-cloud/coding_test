class Solution(object):
    def maxSubArray(self, nums):
        max_num = float('-inf')
        current_num = 0
        for num in nums:
            current_num += num
            if current_num > max_num:
                max_num = current_num
            if current_num < 0:
                current_num = 0
        return max_num
