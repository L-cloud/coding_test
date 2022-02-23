from typing import List
class Solution:
    def __init__(self):
        self.dp = {1: {"()"}}

    def generateParenthesis(self, n: int) -> List[str]:
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = {"(" * n + ")" * n}
        middle = 1
        for str_ in self.generateParenthesis(n - 1):
            candi1 = "()" + str_
            candi2 = str_ + "()"
            self.dp[n].add(candi1)
            self.dp[n].add(candi2)

        while middle < n:
            for str_ in self.generateParenthesis(n - middle):
                candi = "(" * middle + str_ + ")" * middle
                self.dp[n].add(candi)
                for str_2 in self.generateParenthesis(middle):
                    self.dp[n].add(str_ + str_2)
            middle += 1

        return sorted(self.dp[n])