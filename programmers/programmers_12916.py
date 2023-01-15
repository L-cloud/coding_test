import re
def solution(s:str):
    return len(re.sub('p','',s.lower())) == len(re.sub('y','',s.lower()))
