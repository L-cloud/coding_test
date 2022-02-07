class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        dq = [[nums[0],0],[nums[1],1]]
        dp = [0 for _ in range(len(nums))]
        dp[0] = dq[0][0]
        dp[1] = dq[1][0]
        while dq:
            tempt = []
            while dq:
                money, index = dq.pop()
                if nums[index + 2:]:
                    if  dp[index + 2] < money + nums[index + 2]:
                        tempt.append([money + nums[index + 2], index + 2])
                        dp[index + 2] = money + nums[index + 2]
                if nums[index + 3:]:
                    if  dp[index + 3] < money + nums[index + 3]:
                        tempt.append([money + nums[index + 3], index + 3])
                        dp[index + 3] = money + nums[index + 3]
            for _ in range(len(tempt)):
                money, index = tempt.pop()
                if dp[index] <= money:
                    dq.append([money, index])
        return max(dp)
