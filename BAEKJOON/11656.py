import sys

text = sys.stdin.readline().strip()

array = [text[i :] for i in range(len(text))]

for a in sorted(array):
    print(a)
