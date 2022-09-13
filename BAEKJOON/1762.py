import sys
input = sys.stdin.readline
N,M = map(int,(input().split()))
t = set(input().rstrip() for _ in range(N))
tempt = []
for _ in range(M):
    n = input().rstrip()
    if n in t:
        tempt.append(n)

print(len(tempt))
print('\n'.join(sorted(tempt)))

