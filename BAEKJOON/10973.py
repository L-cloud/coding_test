import sys


N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
swap = -1
for i in range(N-1,0,-1):
    if num[i] < num[i-1]:
        swap = i -1
        break
if swap == -1:
    print(-1)
    exit()
index = num.index(1) # 그냥 일단 최소값으로 함
for i in range(N-1, swap , -1):
    if num[i] < num[swap] and num[index] < num[i]: # swap보다는 작은 것 중에서 가장 큰 값
        index = i

num[index], num[swap] = num[swap],num[index]
num = num[:swap+1] + sorted(num[swap+1:], reverse=True)
print(*num)
