class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child, coockies,  = 0, 0
        while child < len(g) and coockies < len(s): 
            if s[coockies] >= g[child]:
                child += 1
            coockies += 1
        return child
