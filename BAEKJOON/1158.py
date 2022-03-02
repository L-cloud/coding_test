import sys

n, k = map(int, sys.stdin.readline().split())
josephus = [i + 1 for i in range(n)]
num,tempt  = 0, -1

