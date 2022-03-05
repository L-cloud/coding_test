import sys
# git add 해야함
# 중첩 괄호가 있을 경우 문제임
#((a+b)*(c*d)/e+(d+k)) flag_stack에 들어가버려서.. 문제
# 반례 찾음 
#((a*b+c))
cal = sys.stdin.readline().strip()
abc_stack, cal_stack = [], []
for char_ in cal:
    if char_.isalpha():
        abc_stack.append(char_)
    else:
        if char_ == "(":
            cal_stack.append("(")
        
        elif char_ == "+" or char_ == '-':
            while cal_stack and cal_stack[-1] != "(":
                abc_stack.append(cal_stack.pop())
            cal_stack.append(char_)

        
        elif char_ == ")":
            while cal_stack:
                pop_ = cal_stack.pop()
                if pop_ == "(":
                    break
                abc_stack.append(pop_)
        else: # char_ == "*" or "/"
            if cal_stack and (cal_stack[-1] == '*' or cal_stack[-1] == "/"):
                abc_stack.append(cal_stack.pop())
            cal_stack.append(char_)


while cal_stack:
    pop_ = cal_stack.pop()

print("".join(abc_stack))