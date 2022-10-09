
# 가상 닉네임
# 채팅방 나가고 새로운 닉네임, 채팅 방에서 닉네임 변경

#닉네임 변경 -> 치곤 채팅방 출력된 메세지 닉네팀도 전부 변경
# 채팅방 중복 닉네임 허용
# 1~10만 
from typing import List
def solution(record:List[str]) -> List[str]:
    answer = []
    dic = {}
    for r in record:
        if len(r.split()) == 3:
            cmd,uid,nick = r.split()
        else:
            cmd,uid = r.split()
        if cmd == 'Enter':
            dic[uid] = nick
            answer.append(['{}님이 들어왔습니다.',uid])
        elif cmd == 'Leave':
            answer.append(['{}님이 나갔습니다.',uid])
        else:
            dic[uid] = nick
    return [s.format(dic[uid]) for s,uid in answer]  
