# x의 길이 = 0<= x <len(s)
# 이건 조금 생각이 필요하네
# 1000000 100만이라.. 10000이면
def solution(s:str):
    s = [i for i in s]
    ans = 0
    for i in range(len(s)):
        t = s[i:] + s[:i]
        stack = []
        for j in t:
            if j == ']':
                if not stack or stack.pop() != '[':
                    break
            elif j == ')': 
                if not stack or stack.pop() != '(':
                    break
            elif j == '}':
                if not stack or stack.pop() != '{':
                    break
            else:
                stack.append(j)
        else:
            if not stack:
                ans += 1
    return ans
