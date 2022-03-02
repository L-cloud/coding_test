import sys

for _ in range(int(sys.stdin.readline())):
    str_list = map(lambda x : x[::-1],(sys.stdin.readline().split()))
    print(' '.join(str_list))
