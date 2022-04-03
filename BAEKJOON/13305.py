import sys

N = int(sys.stdin.readline())

distance = list(map(int, sys.stdin.readline().split()))

gas = list(map(int, sys.stdin.readline().split()))

min_value, cost = gas[0], 0

for i, v in enumerate(distance):
  if  gas[i] < min_value: #현재 주유소가 더 쌈  
    cost += gas[i] * v
    min_value = gas[i]
  else: # 이전의 가스가 더 쌈
    cost += min_value * v

print(cost)
