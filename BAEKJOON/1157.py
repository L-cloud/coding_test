import collections
s = collections.Counter(input().upper()).most_common()
print("?" if 1 < len(s) and s[0][1] == s[1][1] else s[0][0])
