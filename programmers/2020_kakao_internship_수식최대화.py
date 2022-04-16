import sys,itertools

expression = sys.stdin.readline().rstrip()
stack,tempt,operators = [], [], set()
output = 0
for e in expression:
    if e.isdigit():
        tempt.append(e)
    else:
        stack.append("".join(tempt))
        tempt = []
        operators.add(e)
        stack.append(e)
stack.append("".join(tempt))

for op in itertools.permutations(operators,len(operators)):
    tempt = stack[:]
    for o in op:
        index = 0
        while index < len(tempt):
            if tempt[index] != o:
                index += 1
            else:
                print(" ".join(tempt[index -1 : index +2]))
                num = str(eval(" ".join(tempt[index -1 : index +2])))
                for _ in range(3):
                    del tempt[index -1]
                tempt.insert(index-1,num)
    output = max(output, abs(int(tempt[0])))

print(output)


            
