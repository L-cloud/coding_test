import sys
import functools

num = int(sys.stdin.readline())
if num > 1:
    fac = functools.reduce(lambda x,y: x*y,range(1,num + 1))
else: 
    fac = 1
print(fac)