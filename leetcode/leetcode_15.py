import itertools
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output =[]
        for i in set(itertools.combinations(nums, 3)):
            i = sorted(i)
            if sum(i) == 0 and i not in output:
                output.append(i)
        return output
