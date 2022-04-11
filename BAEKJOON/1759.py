import sys, itertools


def password(consonant_num:int, vowels_num:int):
    for c in itertools.combinations(consonant,consonant_num):
        for v in itertools.combinations(vowels,vowels_num):
            output.append("".join(sorted(list(c)+list(v))))
L, C = map(int,sys.stdin.readline().split())
consonant = list(map(str,sys.stdin.readline().split()))
vowels,output = [],[]
for c in consonant:
    if c in  {'a','e','i','o','u'}:
        vowels.append(c) # 여기서 지우면 체크 for문 안 도는 녀석 있어서 안 댐
for v in vowels:
    consonant.remove(v)
consonant.sort()
vowels.sort()
consonant_num, vowels_num = L - 1, 1
while len(consonant) < consonant_num:
    consonant_num -= 1
    vowels_num += 1
while 1 < consonant_num  and  vowels_num <= len(vowels):
    password(consonant_num,vowels_num)
    consonant_num -= 1
    vowels_num += 1
for o in sorted(output):
    print(o)
# consonant 최소 2개, vowels 최소 1개
