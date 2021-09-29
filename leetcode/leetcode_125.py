import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9a-zA-Z]',"",s).lower()
        return s == s[::-1]

# if you want pop()
# use isalnum() then compare pop() == pop(0) while len(str(num or char)) > 1
