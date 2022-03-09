import sys

zin, b = sys.stdin.readline().split()

b = int(b)

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_dic = {}
num = 0
for i, v in enumerate(alpha, 10):
    alpha_dic[v] = i

for i,v in enumerate(zin[::-1]):
    if v.isalpha():
        v = alpha_dic[v]
    num += int(v) * b ** i

print(num)