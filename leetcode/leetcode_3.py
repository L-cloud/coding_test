class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        substring = []
        for index,char in enumerate(s):
            if char in substring:
                substring = substring[substring.index(char) + 1 :]
            substring.append(char)
            if max_len < len(substring):
                max_len = len(substring)
        return max_len




