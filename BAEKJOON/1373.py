from operator import index
import sys
import collections
binary = sys.stdin.readline().strip()[::-1]
dq,index = collections.deque(), 0
while index < len(binary):
    num = 0
    tempt = binary[index : index+3]
    for i, v in enumerate(tempt):
        num += int(v)*2**int(i)
    dq.appendleft(num)
    index += 3
print("".join(map(str,dq)))
    
 