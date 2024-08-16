import sys
input = sys.stdin.readline
s = input()
n = int(input())
arr = [input()   for _ in range(n)]
print(sum([1 for i in arr if i[:5] == s[:5 ]]))
