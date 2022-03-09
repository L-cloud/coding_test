
import sys
# 아 괜히 어렵게 생각.. 이거 소수를 찾을 필요가 없이 그냥 for 문으로 계속 나눠주기만 하면 됨...
# 어짜피 2로 계속 나누면 2의 배수들이나 2로 나눠지는 것들로 그 수를 못 나누니까!!


num = int(sys.stdin.readline())

for i in range(2, num + 1):
    if num % i == 0:
        while num % i == 0:
            print(i)
            num //= i
    
    if num <= 1:
        break


