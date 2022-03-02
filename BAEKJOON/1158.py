from itertools import count
import sys

n, k = map(int, sys.stdin.readline().split())
josephus = [i + 1 for i in range(n)]
index, num = -1, 0
print("<", end= "")
while num != len(josephus):
    cnt = 0
    while cnt < k:
        index = (index + 1) % n
        if josephus[index] != None:
            cnt += 1
    if num == len(josephus) - 1:
        print(josephus[index], end = "")
    else:
        print(josephus[index], end = ", ")
    josephus[index] = None
    num += 1
print(">")



