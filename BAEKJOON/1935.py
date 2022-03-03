import sys

cal_num = int(sys.stdin.readline())
cal = sys.stdin.readline().strip()
num_stack, stack, index = [] , [], 0
alpha_set = {}
for _ in range(cal_num):
    num_stack.append(int(sys.stdin.readline()))

for char in cal:
    if char.isalpha():  
        if char not in alpha_set:
            alpha_set[char] = num_stack[index]
            index += 1
        stack.append(alpha_set[char])
    else: # 연산
        b , a = stack.pop(), stack.pop() # 한줄에 pop() 두 개 할 때 주의! 어떤게 먼저 되는지 가장 왼쪽부터 순서가 되는거임!
        if char == '+':
            stack.append(a + b)
        elif char == '-':
            stack.append(a - b)
        elif char == '*':
            stack.append(a * b)
        else: # char == '/'
            stack.append(a / b)
        
    

print('%0.2f' % stack[0])




