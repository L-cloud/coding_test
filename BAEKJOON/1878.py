import sys
from collections import deque
sequence = []
for _ in range(int(sys.stdin.readline())):
    sequence.append(int(sys.stdin.readline()))
stack, num  = [], deque([i  + 1 for i in range(len(sequence))])
print_stack, flag = [], True
for i in sequence:
    while num and num[0] <= i:
        stack.append(num.popleft())
        print_stack.append("+")
    if stack and stack[-1] == i:
        stack.pop()
        print_stack.append("-")
        continue
    print('NO')
    flag = False
if flag:
    for signal in print_stack:
        print(signal)