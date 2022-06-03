import sys
# 마이너스 나오면 거기서부터 + 나올 때 까지 더한다. 
# 더하기는 그냥 한다. (마이너스 최대화 시켜줌
s = sys.stdin.readline().strip()
ops = s.split('-')
for index,op in enumerate(ops):
    n,tempt= "", 0
    for i in op:
        if i.isalnum():
            n += i
        else:
            tempt += int(n)
            n = ""
    if n:
        tempt += int(n)
    ops[index] = tempt
answer = ops[0]
for i in range(1, len(ops)):
    answer -= ops[i]
print(answer)





