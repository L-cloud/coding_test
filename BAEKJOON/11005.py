import sys
import collections
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
stack = collections.deque() 
num, b = map(int, sys.stdin.readline().split())

while 0 < num:
    remainder = num % b
    num //= b
    if 10 <= remainder:
        remainder = alpha[remainder - 10]
    stack.appendleft(remainder)

print("".join(map(str,stack)))

    
    
    