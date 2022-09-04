import sys,bisect
input = sys.stdin.readline
N = int(input())
cords,index = {},{}
for _ in range(N):
    value, key = map(int, input().split()) # value 시작시점, key 도착지점
    cords[key] = value
    index[value] = 0 # 시작 지점에 대한 인덱스 일단 0으로
l = [0]

for key in sorted(cords.keys()):
    if l[-1] < cords[key]:
        l.append(cords[key])
        index[cords[key]] = len(l) - 1
    else:
        index[cords[key]] = bisect.bisect_left(l,cords[key])
        l[index[cords[key]]] = cords[key]
m = max(index.values())
for key in sorted(cords.keys(),reverse= True):
    if index[cords[key]] == m:
        index[cords[key]] = False
        m -= 1
l = [key for key in index if index[key]]
print("\n".join(map(str,[len(l)] + sorted(l))))

