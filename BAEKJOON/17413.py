import sys

s = sys.stdin.readline()
empty_list = []
start, end = 0, 0
while end < len(s):
    if s[end] == " ": #띄어쓰기 없이 그냥 생문자로만 나올 수도 있음
        empty_list.append(s[start:end][::-1]+" ")
        end += 1
        start = end
    elif s[end] == '\n':
        empty_list.append(s[start:end][::-1])
        end += 1
    elif s[end] == '<':
        if start != end:
            empty_list.append(s[start:end][::-1])
        start = end
        bracket_index = s.index('>',start)
        empty_list.append(s[start:bracket_index + 1])
        start = end = bracket_index + 1
    else:
        end += 1

print("".join(empty_list))

    
    

        
    