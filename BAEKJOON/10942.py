import sys

str_len = sys.stdin.readline()

str_ = list(sys.stdin.readline().split())
for _ in range(int(sys.stdin.readline())):
    start, end = map(int, sys.stdin.readline().split())
    palindrome = True
    while start <= end:
        if str_[start - 1] != str_[end - 1]:
            palindrome = False
            break
        start += 1
        end -= 1

    if palindrome:
        print(1)
    else:
        print(0)
