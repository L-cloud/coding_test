N = int(input())

def star(N):
    if N == 3:
        s = ["  *  "," * * ","*****"]
        return s
    s = []
    arr = star(N // 2)
    for i in arr:
        s.append(" " * (N//2) + i + " "*(N//2))
    for i in arr:
        s.append(i + " " + i)
    return s

s = star(N)
print("\n".join(s))