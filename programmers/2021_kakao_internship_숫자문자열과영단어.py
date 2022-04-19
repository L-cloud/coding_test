def solution(s):
    dic = {'zero' : 0, 'one' : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    answer = []
    index = 0 
    while index < len(s):
        tempt = []
        while index < len(s) and s[index].isalpha() and "".join(tempt) not in dic:
            tempt.append(s[index])
            index += 1
        if tempt:
            answer.append(dic["".join(tempt)])
        else:
            answer.append(s[index])
            index += 1
    return int(''.join(map(str,answer)))
