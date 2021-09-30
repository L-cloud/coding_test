import collections
import re
from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-z0-9A-Z\s]',' ', paragraph).lower() # remove special character
        paragraph_count = collections.Counter(paragraph.split())
        for key,value in paragraph_count.most_common(len(paragraph)):
            if key not in banned:
                return key


class Solution : # other version
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph =[paragraph for paragraph in re.sub((r'[^\w]'),' ',paragraph.lower().split()) if paragraph not in banned]
        counts = collections.Counter(paragraph)
        return counts.most_common(1)[0][0]

