def solution(s:str)->int:
    answer = 1
    for i,v in enumerate(s):
        for j in range(i):
            if i-j + 1 < answer:
                break
            left,right = j,i
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    continue
                break
            if right <= left:
                answer = max(i-j + 1,answer)
    return answer
