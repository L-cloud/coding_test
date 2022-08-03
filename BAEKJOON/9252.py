import sys
        input = sys.stdin.readline
s1 = input().rstrip()
s2 = input().rstrip()
prev = [[] for _ in range(len(s1) + 1)]
current = [[] for _ in range(len(s1) + 1)]
for v1 in s2:
    for index, v2 in enumerate(s1,1):
        if v1 == v2:
            current[index] = prev[index - 1] + [v2]
        else:
            current[index] = current[index -1] if len(prev[index]) < len(current[index -1]) else prev[index]
    prev,current = current, prev
prev.sort(key = lambda x: len(x), reverse = True)
print(len(prev[0]))
print("".join(prev[0]))
