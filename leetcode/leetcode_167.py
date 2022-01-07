class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            candi = bisect.bisect_left(numbers,target - num, index + 1,len(numbers))
            if candi < len(numbers) and numbers[candi] + num == target:
                return [index + 1, candi + 1]
