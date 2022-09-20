from typing import List
def solution(matrix_sizes:List[int]) -> int:
    dp = [[0]* len(matrix_sizes) for _ in range(len(matrix_sizes))]
    for i in range(1,len(dp)):
        for j in range(len(dp) - i):
            min_value = float('inf')
            for k in range(j,i+j):
                min_value = min(min_value, dp[j][k] + dp[k+1][i+j] + matrix_sizes[j][0] * matrix_sizes[k][1] * matrix_sizes[i+j][1])
            dp[j][i+j] = min_value 
    return dp[0][-1]


from typing import List
from collections import deque,Counter
def solution(gems:List[str]) -> List[int]:
    g,cnt,q = len(set(gems)),Counter(), deque()
    answer = [0,100001]
    for index,value in enumerate(gems,1):
        cnt[value] += 1
        q.append([value,index])
        if value == q[0][0]:
            while 1 < cnt[q[0][0]]:
                cnt[q[0][0]] -= 1
                q.popleft()
        if len(cnt) == g:
            if q[-1][1] - q[0][1] < answer[1] - answer[0]:
                answer = [q[0][1],q[-1][1]]
    return answer

