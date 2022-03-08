import sys
def get_gcd(a:int,b:int) -> int :
    if b == 0:
        return a
    gcd = get_gcd(b, a % b)
    return gcd


N, S = map(int, sys.stdin.readline().split())
brothers = sorted(list(map(int, sys.stdin.readline().split())))
max_d = abs(brothers[0] - S)
for i in range(len(brothers) - 1):
    diff = brothers[i + 1] - brothers[i]
    diff = get_gcd(max(diff, max_d), min(diff, max_d))
    max_d = min(diff, max_d)
    
print(max_d)
