import sys
from typing import List
def demical(a : int,num :int, board:List[int]) -> bool :
    if not board[num - a]:
        return False
    index, flag = 2, True
    while index * index <= num:
        if num % index == 0:
            flag = False
            break
        index += 1
    if flag:
        board[num - a] = True
        index = 2
    else: 
        index = 1
    while index*num -a < len(board):
        board[index*num - a] = False
        index += 1
    return board[num - a]
a, b = map(int, sys.stdin.readline().split())
board = [True for _ in range(a,b+1)]
for num in range(a, b+ 1):
    if num > 1 and demical(a,num, board):
        print(num)

# 2번째 방법
import sys 
import math
a, b = map(int, sys.stdin.readline().split())
board = [True for _ in range(b + 1)]

for num in range(2, int(math.sqrt(b) + 1)):
    if board[num]:
        index = 2

        while(num*index) <= b:
            board[num*index] = False
            index += 1

for index in range(a, b + 1):
    if index > 1 and board[index]:
        print(index)
    


    
        