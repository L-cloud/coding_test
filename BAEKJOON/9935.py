import sys
input = sys.stdin.readline
s = input().rstrip()
p = input().rstrip()
s_list, s_idx, p_idx = [],0,0
while s_idx < len(s):
    s_list.append(s[s_idx])
    s_idx += 1
    if s_list[-1] == p[p_idx]:
        p_idx += 1
        if  len(p) == p_idx:
            while p_idx:
                s_list.pop()
                p_idx -= 1
            p_idx = 0
            for i in s_list[-len(p):]:
                if i == p[p_idx]:
                    p_idx +=1
                else:
                    p_idx = 1 if i == p[0] else 0
    else:
        p_idx = 1 if s_list[-1] == p[0] else 0
if s_list:
    print("".join(s_list))       
else:
    print("FRULA")