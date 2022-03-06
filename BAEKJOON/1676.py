import sys
import functools
from tkinter import N
num = int(sys.stdin.readline())
if num > 1:
    fac = functools.reduce(lambda x,y: x*y,range(1,num + 1))
else: 
    fac = 1
fac = str(fac)[::-1]
index = 0 
while fac[index] == '0':
    index += 1
print(index)

# 2번째 방법
# 팩토리얼이기 때문에 5로 나눠서 떨어지는 수가 몇 개인지 확인 하면 된다.
# 100 // 5 = 20 인데 여기서 20도 5로 나누어 떨어지기 때문에 더해줘야함 이라고 하는데
# 사실 잘 이해가 안 간다.. 
n = int(sys.stdin.readline())

cnt = 0 
while n!= 0:
    n //= 5
    cnt += n
print(cnt)
