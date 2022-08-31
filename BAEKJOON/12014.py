import sys,bisect
input = sys.stdin.readline
for T in range(int(input())):
    N,M = map(int,input().split())
    tempt = []
    for stock in map(int,input().split()):
        index = bisect.bisect_left(tempt,stock)
        if  len(tempt) - 1 < index: 
            tempt.append(stock)
            continue
        tempt[index] = stock
    print(f"Case #{T + 1}")
    print(1 if  M -1 < len(tempt)  else 0)

