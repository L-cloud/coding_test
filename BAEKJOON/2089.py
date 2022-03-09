import sys


a, b = map(int, sys.stdin.readline().split())

b = min(b, a - b)

two, five = 0, 0

for num in range(a, b, -1):
    while num % 2 == 0:
        two += 1
        num //= 2
    while num % 5 == 0:
        five += 1
        num //= 5

for num in range(b, 1, -1):
    while num % 2 == 0:
        two -= 1
        num //= 2
    while num % 5 == 0:
        five -= 1
        num //= 5

print(min(two, five))
