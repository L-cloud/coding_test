from typing import List
def solution(m:str, musicinfos:List[str]) -> str:
    m = abc(m)
    m_t, ans = 0, "(None)"
    for info in musicinfos:
        info = info.split(",")
        t = c_t(info[0],info[1])
        code = abc(info[3])
        code = code[:t] if t < len(code) else code * (t // len(code)) + code[:t % len(code)]
        print(code)
        if find(m,code) and  m_t < t:
            ans = info[2]
            m_t = t
    return ans

def c_t(s1:str,s2:str) -> int:
    h1,m1 = s1.split(":")
    h2,m2 = s2.split(":")
    return int(h2) * 60 + int(m2) - (int(h1) * 60 + int(m1))

def abc(s:str) -> List[str]:
    stack, i = [], 0
    while i < len(s):
        if i + 1 < len(s) and s[i+1] == '#':
            stack.append(s[i:i+2])
            i += 2
            continue
        stack.append(s[i])
        i+= 1
    return stack

def find(m:List[str], code:List[str]) -> bool:
    i = 0
    for c in code:
        if c == m[i]:
            i += 1
        else:
            i = 1 if c == m[0] else 0
        if i == len(m):
            return True
