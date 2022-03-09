import sys

stack,max_num = [], 0
while True: 
    num = int(sys.stdin.readline())
    if num == 0:
        break
    max_num = max(num, max_num)
    stack.append(num)

dp = [True] * (max_num + 1)
demical_index = []
for i in range(2, max_num + 1):
    index = 2
    while index * i <= max_num:
        dp[index * i] = False
        index += 1

for i in range(3, max_num + 1):
    if dp[i]:
        demical_index.append(i)


for num in stack:
    flag = False
    for demical in demical_index:
        if num < demical - 3:
            break
        if dp[num - demical]:
            print(num,'=',num - demical,"+" ,(demical))
            flag = True
            break
    if not flag:
        print( "Goldbach's conjecture is wrong.")