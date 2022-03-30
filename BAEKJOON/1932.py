import enum
from random import triangular
import sys, collections
num = int(sys.stdin.readline())
triangle = []
stair = collections.defaultdict(list)
for _ in range(num):
    triangle.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, num):
    for index, value in enumerate(triangle[i]):
        tempt = []
        if index == 0: # first
            triangle[i][index] += triangle[i-1][index] 
        elif  index == len(triangle[i]) - 1: # last
            triangle[i][index] += triangle[i-1][index -1]
        else: # 0< index < len(triangle) - 1
           triangle[i][index] += max(triangle[i -1][index - 1], triangle[i -1][index])

print(max(triangle[-1]))