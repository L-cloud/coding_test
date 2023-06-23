from typing import List
def solution(sequence:List[int]) -> int:
    answer, l = 0, [1,-1]
    s = [[0,0]] # indexm sum
    for n in sequence:
        t,v = [],{}
        for _ in range(len(s)):
            i, total = s.pop()
            if n*l[i] + total < 0: # 0보다 작음 그럼 버려
                t.append([i,n*l[(i+1)%2]])
                answer = max(n*l[(i+1)%2], answer)
                v[i] = max(v.get(i,0),n*l[(i+1)%2] )
            else: # 그런데 0보다 작지 않더라도 여기서 시작하는 녀석이 더 클 수 있음.. 그럼 어떻게 해야하나
                total += n*l[i]
                t.append([(i+1) %2,total])
                answer = max(answer,total)
                v[(i+1) %2] = max(v.get((i+1) %2,0), total)
                if 0 < n * l[(i+1) %2]:
                    # 나랑 반대의 부호 녀석만 있겠지
                    if i not in v: # 반대되는 녀석이 없음
                        t.append([i,n * l[(i+1) %2]])
                        answer = max(answer,n * l[(i+1) %2])
                        v[i] = max(v.get(i,0),n*l[(i+1)%2] )
        s = [[i,k] for i,k in v.items()]
    return answer
