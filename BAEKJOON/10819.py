import sys
from typing import List
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
output,i = [0],0
order = []

def order_sum(tempt:List[int], num_list:List[int]) -> int:
    if not num_list:
        tempt_sum = 0
        for i in range(len(tempt) - 1):
            tempt_sum += abs(tempt[i] - tempt[i + 1])
        output[0] = max(tempt_sum,output[0])
    for i,v in enumerate(num_list):
        tempt.append(v)
        order_sum(tempt,num_list[:i]+num_list[i+1:])
        tempt.pop()
order_sum([],num_list)
print(output[0])