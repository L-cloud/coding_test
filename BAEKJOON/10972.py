from typing import List
import sys
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
permutation = list(map(int, sys.stdin.readline().split()))
def next_permutation(tempt:List[int],index:int,visited:set,flag : bool):
    if len(permutation) == index:
        if tempt == permutation:
            return True # 지금 순열 만듦
        else:
            print(*tempt)
            exit()
 # 입력 받은 순열까지 만들었는지 아닌지 check
    for i in range(1,N+1):
        if not flag:
            if i != tempt[index]:
                continue
            if next_permutation(tempt, index +1,visited,flag):
                flag = True
                tempt.pop()
                visited.remove(i)
                continue
        if flag and i not in visited: 
            tempt.append(i)
            visited.add(i)
            next_permutation(tempt, index +1,visited,flag)
            tempt.pop()
            visited.remove(i)
    return flag
if permutation[::-1] == list(range(1,N+1)):
    print(-1)
    exit()
next_permutation(permutation[:],0,set(permutation),False)
print(-1)     
