class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len,sub = 0, []
        for char in s:
            if char not in sub:
                sub += [char]
                max_len = max(max_len, len(sub))
            else:
                sub = sub[sub.index(char) + 1:] + [char]
        return max_len