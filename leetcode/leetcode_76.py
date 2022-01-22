import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0 # 와 여기가 지리는 코드
            need[char] -= 1
            
            if missing == 0: # 이미 다 채워졌을 때 다듬으면 되는데.. 이걸 왜 고려 안 했지..
                while left < right and need[s[left]] < 0 :
                    need[s[left]] += 1
                    left += 1
                if not end or right - left <= end - start:
                    start, end = left, right
                # 일단 최소값 저장 했으니 다음 값도 나올거 찾기 위해 1칸 씩 이동
                need[s[left]] += 1
                missing += 1
                left += 1
                
        return s[start : end]


