def solution(s):
    s = s[1:len(s)-1] # 앞 뒤 {} 제거
    i,answer = 0,[]
    stack = []
    while i < len(s):
        while s[i] == "{":
            i += 1
        index = i
        while s[i] != "}":
            i += 1
        stack.append(list(map(int,s[index : i].split(","))))
        i += 2 # , 지나가야함
    stack.sort(key = lambda x:len(x))
    for i in stack:
        for j in i:
            if j not in answer:
                answer.append(j)
                break
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))