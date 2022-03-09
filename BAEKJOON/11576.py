import sys
import collections
future, now = map(int, sys.stdin.readline().split())
digit = int(sys.stdin.readline()) - 1
num_list = list(map(int, sys.stdin.readline().split()))
ten, stack = 0, collections.deque()

for num in num_list:
    ten += num*future**digit
    digit -= 1
while 0 < ten:
    stack.appendleft(ten % now)
    ten //= now

if not stack:
    print(0)
else:
    print(" ".join(map(str, stack)))
    

    
