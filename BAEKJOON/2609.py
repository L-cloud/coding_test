from re import T
import sys

a, b = map(int, sys.stdin.readline().split())
max_factor = 1
for i in range(1, min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        max_factor = i

a_index, b_index = 1,1
while a*a_index != b*b_index:
    if a*a_index < b*b_index:
        a_index += 1
    else:
        b_index += 1

print(max_factor)
print(a*a_index )