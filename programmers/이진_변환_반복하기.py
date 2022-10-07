
import re
def solution(s:str):
    answer = [0,0]
    while s != '1': # 0을 제거한다 -> 길이만큼 수를 2진수로 바꾼다. 반복
        answer[0] += 1 # trie 횟수
        t_s = re.sub('0','',s)
        answer[1] += len(s) - len(t_s) # 0갯수
        s = bin(len(t_s))[2:]        
    return answer
