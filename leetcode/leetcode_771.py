class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = collections.Counter(stones)
        output = 0
        for jewel in jewels:
            output += stones[jewel]
        return output
