import sys
import collections
octocal = sys.stdin.readline().strip()
stack = []
for oc in octocal:
    oc = int(oc)
    tempt = ""
    while 0 < oc:
        tempt = str(oc % 2) + tempt
        oc //=2
    tempt = tempt.zfill(3)
    stack.append(tempt)
stack = ''.join(stack)
index = 0
while stack[index] == "0":
    index += 1
if stack[index :]:
    print(stack[index:])
else:
    print(0)