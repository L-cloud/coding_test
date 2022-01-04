class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(list(map(str,nums)),reverse = True)
        for index1,num1 in enumerate(nums): # bubble sort
            for index2,num2 in enumerate(nums[index1:]):
                if num1[0] != num2[0]:
                    break
                if num1 + num2 < num2 + num1:
                    nums[index1], nums[index1 + index2] = nums[index1+index2], nums[index1]
        
                
        if nums[0] == '0':
            return '0'
        return "".join(nums)


