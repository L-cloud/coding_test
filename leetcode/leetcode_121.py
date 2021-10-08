from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value, max_profit = prices[0], 0
        for price in prices:
            if price < min_value:
                min_value = price
            else:
                if max_profit < price - min_value:
                    max_profit = price - min_value
        return max_profit

class Solution: # simple ver
    def maxProfit(self, prices: List[int]) -> int:
        min_value, max_profit = float('inf'), 0
        for price in prices:
            min_value = min(price, min_value)
            max_profit = max(max_profit, price - min_value)
        return max_profit