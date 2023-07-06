from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
matrix = Counter(list(map(int,input().split())))
l = int(input())
print(*[matrix[k] for k in list(map(int,input().split()))])
