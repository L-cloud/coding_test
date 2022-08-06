import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# visited 이거나 원하는게 자기 자신이거나
def make_group(v:set(),i : int) -> bool:
    if visited[i]:
        return False
    v.add(i)
    visited[i] = True
    if wanted[i] in v:
        v.remove(wanted[i])
        group[i] = True
        return True
    else:
        is_group = make_group(v,wanted[i])
        if is_group and wanted[i] in v:
            v.remove(wanted[i])
            group[i] = True
            return True
        else:
            return False

T = int(input())
for _ in range(T):
    N = int(input())
    group = [False for _ in range(N + 1)]
    visited = [False for _ in range(N+1)]
    wanted = [0]
    wanted +=list(map(int,input().split()))
    for i in range(1,N+1):
        if not visited[i]:
            make_group(set(),i)
    print(sum([1 for i in range(1,N+1) if not group[i]]))


