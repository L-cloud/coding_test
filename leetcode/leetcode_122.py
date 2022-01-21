from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev, total = prices[0], 0
        for price in prices:
            if prev < price:
                total += price - prev
                prev = price
            else: # price < prev
                prev = price
        return total