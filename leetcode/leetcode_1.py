from typing import List
class Solution: #Brute force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for inner_index, inner_value in enumerate(nums[index + 1:]):
                if nums[index] + inner_value == target:
                    return [index, inner_index + index + 1]

    def twoSum(self, nums: List[int], target: int) -> List[int]:# using in
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]

    def twoSum(self, nums: List[int], target: int) -> List[int]:  # dict
        nums_map = {}
        # switch index and value
        for i ,num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
