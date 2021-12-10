import copy
def solution(begin, target, words):
    if target in words:
        words.remove(target)
        words.append(target)
    else:
        return 0
    answer = float('inf')
    stack,index = [[begin, 0]],0
    while stack:
        tempt = []
        while stack:
            word, attempt = stack.pop()
            if word == target:
                answer = min(attempt,answer)
            elif index < len(words):
                if differ(word, words[index]):
                    print(word,words[index])
                    tempt.append([words[index], attempt + 1])
                    tempt.append([word,attempt])
                else: # 1개 이상 차이
                    tempt.append([word,attempt])
        stack = copy.deepcopy(tempt)
        index += 1
    
    return answer


def differ(word1,word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
            if cnt > 1:
                return False
    return True
