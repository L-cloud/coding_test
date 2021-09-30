from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit= [], []
        for log in logs:
            log = log.split()
            if log[1].isalpha():
                letter.append(log)
            else:
                digit.append(" ".join(log))
        letter.sort(key = lambda x : (x[1:],x[0]))
        letter = list(map(lambda x : " ".join(x), letter))
        letter += [i for i in digit]
        return letter

# better one
from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.spilt()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key = lambda x:(x.split()[1:], x.split()[0]))
        return letters + digits