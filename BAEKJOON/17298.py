import sys

num = [-1 for _ in range(int(sys.stdin.readline()))]

sequence = list(map(int, sys.stdin.readline().split()))

stack = []

for i in range(len(num)):
    while stack and sequence[stack[-1]] < sequence[i]:
        num[stack.pop()] = sequence[i]
    stack.append(i)
print(" ".join(map(str, num)))
