# import collections
#
# class Solution(object):
#     def sortColors(self, nums): # using counter version
#         count = collections.Counter(nums)
#         index = 0
#         for i in range(3):
#             for _ in range(count[i]):
#                 nums[index] = i
#                 index += 1

import collections

class Solution(object):
    def sortColors(self, nums): # using pointer, 답지 참고함..
        index,left, right = 0,0, len(nums) - 1
        while index <= right:
            if nums[index] == 0:
                nums[index],nums[left] = nums[left],nums[index]
                index += 1 #정렬하면서 앞으로 나가니까 2가 있을 일이 없음... 그래서 index += 1 해도 안심
                left += 1
            elif nums[index] == 2:
                nums[index],nums[right] = nums[right],nums[index]
                right -=1
            else:
                index += 1


