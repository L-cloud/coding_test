import math
class Solution:
    def climbStairs(self, n: int) -> int:
        num = 1
        one, two = n - 2, 1
        while one >= 0:
            num += self.nCr(one + two, two)
            one -= 2
            two += 1
        return num
    
    def nCr(self,n,r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)
