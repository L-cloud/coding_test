from typing import List
from functools import reduce
import collections
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            count = collections.Counter(nums)
            if count[0] > 1:
                return [0] * len(nums)
            # num of 0 is one
            index = nums.index(0)
            multi = reduce(lambda x,y:x*y, nums[:index] + nums[index+1:])
            return [multi if i == 0 else 0 for i in nums]
        else:
            muti = reduce(lambda x,y : x*y, nums)
            return [int(muti/i) for i in nums]

        # You must write an algorithm that runs in O(n) time and without using the division operation.


        #No division ver
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            out = []
            p = 1
            for i in range(0, len(nums)):
                out.append(p)
                p = p * nums[i]
            p = 1
            for i in range(len(nums) - 1, - 1, -1):
                out[i] = out[i] * p
                p = p * nums[i]
            return out
