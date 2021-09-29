# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = re.sub('[^0-9a-zA-Z]',"",s).lower()
#         return s == s[::-1]

a = "ABC"
print(id(a), a)
a = a.lower()
print(id(a),a)