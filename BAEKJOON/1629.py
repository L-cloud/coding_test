A, B, C = map(int, input().split())

def check(a,b):
    if b  == 1:
        return a % C
    if b % 2 == 0:
        a1 = check(a, b//2)
        return a1 * a1 % C 
    else:
        a1 = check(a, b // 2)
        return a * a1 * a1 % C

print(check(A,B))