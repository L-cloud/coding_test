import sys
num = int(sys.stdin.readline())

flag = False if num % 2 == 0 else True
num = num -1 if flag else num # 홀수 짝수 구분
def dfs(num : int) -> int:
    exp = 0
    if num < 0:
        while (-2) ** exp > num:
            exp += 1
    else:
        while (-2) ** exp < num:
            exp += 1

    return exp, (-2) ** exp - num

exp, num = dfs(num)
binary = [0] * (exp + 1)
binary[exp] = 1

while num != 0:
    exp, num = dfs(num)
    binary[exp] = 1

if flag:
    binary[0] = 1

print("".join(binary[::-1]))