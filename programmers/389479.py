from typing import List
from collections import deque
def solution(players: List[int], m: int, k: int) -> int:
    '''
    m = 서버 1대가 감당 가능한 인원, default 0대로 m-1명까지 가능
    k = 서버 1대 최소 빌리는 시간
    players = 0~23 길이. 각 인덱스는 게임 플레이어의 수
    
    최소 증설 서버의 갯수는?
    '''
    
    '''
    필요한 것 == 실시간 감당 가능한 수 + 
    흠.. 배열 길이 k 인 것 circular que로 해서.. 할까?
    최대는 k * 24 충분
    '''
    que, answer = deque([],k-1), 0
    for i,player in enumerate(players):
        s = sum(que) + 1
        if player < s * m:
            que.append(0)
        else:
            r = (player - s*m) // m + 1
            answer += r
            que.append(r)
            
    return answer
