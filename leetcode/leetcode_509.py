class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        out, prev1, prev2 = 0 , 0, 1
        for i in range(2, n + 1):
            out = prev1 + prev2
            prev1 = prev2
            prev2 = out
        return out
