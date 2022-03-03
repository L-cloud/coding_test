import sys

bracket = sys.stdin.readline()

que = []
stick = 0
for i,v in enumerate(bracket):
    if v == ")":
        index, value = que.pop()
        if i - index == 1:
            stick += len(que)
        else:
            stick += 1
    else:
        que.append((i,v))

print(stick)