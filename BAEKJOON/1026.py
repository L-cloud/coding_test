import sys
input = sys.stdin.readline
n = int(input())
a, b = sorted(list(map(int,input().split()))), sorted(list(map(int,input().split())),reverse=True)
print(sum([i*j for i,j in zip(a,b)]))

