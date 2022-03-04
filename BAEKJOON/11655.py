from posixpath import split
import sys

abc = "abcdefghijklmnopqrstuvwxyz"
upper_abc = abc.upper()
text = [char for char in sys.stdin.readline()]
for i,v in enumerate(text):
    if v.isalpha():
        if v.isupper():
            alpha = upper_abc[(upper_abc.index(v) + 13) % len(upper_abc)]
            text[i] = alpha
        else:
            alpha = abc[(abc.index(v) + 13) % len(abc)]
            text[i] = alpha

print("".join(text[:len(text) - 1]))

