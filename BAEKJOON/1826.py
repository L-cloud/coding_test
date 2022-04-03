import sys

N = int(sys.stdin.readline())

gas_station = {}
for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  gas_station[a] = b

distance, gas = map(int, sys.stdin.readline().split())
stop,current = 0, gas # 현재 위치
while current < distance :
  gas, station = 0, -1
  for key in sorted(gas_station):
    if current < key:
      break
    if gas < gas_station[key]:
      gas = gas_station[key]
      station = key

  if not gas: # 정류소가 더 이상 없음
    print(-1)
    exit()
  current += gas 
  del gas_station[station]
  stop += 1

print(stop)
