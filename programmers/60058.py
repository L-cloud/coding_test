def solution(p:str) -> str:
    return dfs(p)

def dfs(s:str) -> str:
    if check(s):
        return s
    n1,n2 = 0,0
    for i,v in enumerate(s):
        if v == '(':
            n1 += 1
        else:
            n2 += 1
        if n1 == n2:
            u,v = s[:i+1], s[i+1:]
            break
    u = f"({dfs(v)}){''.join([')' if i == '(' else '(' for i in u[1:-1]])}" if not check(u) else u + dfs(v)
    return u
    
        
def check(s:str) -> bool:
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        elif st and st[-1] == '(':
            st.pop()
        else:
            return False
    return not st
