def solution(s:str) -> int:
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return 0 if stack else 1
