import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output, seen = [], []
        candi = [[collections.Counter(str), index] for index,str in enumerate(strs)]
        for count, index in candi:
            if count in seen:
                continue
            seen.append(count)
            c = []
            for inner_count, inner_index in candi[index:]:
                if count == inner_count:
                    c.append(strs[inner_index])
            output.append(c)
        return output



class Solution: #Better Version
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())