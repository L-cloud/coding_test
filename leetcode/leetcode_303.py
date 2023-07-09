class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.seg = self.make_segment(nums)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.seg[right+1] - self.seg[left]
    
    def make_segment(self, nums:List[int]) -> List[int]:
        t = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            t[i+1] = t[i] + nums[i]
        return t
