import collections
def solution(user_id, banned_id):
    def dfs(user, banned,tempt):
        if not banned:
            cnt.add(tuple(set(user_id) - set(tempt)))# 남아있는 user 지우면 banned 된 아이디만 남음
            return 
        visited = collections.defaultdict(list)
        for i,u in enumerate(user):
            for ban in banned:
                if compare(u,ban):
                    if ban not in visited[u]: # 중복방지 *** 이 2개라면..
                        tempt.append(u)
                        next_banned = banned[:]
                        next_banned.remove(ban)
                        visited[u].append(ban)
                        dfs(user[i + 1 :],next_banned,tempt)
                        tempt.pop()
    cnt = set()
    dfs(user_id,banned_id,[])
    return len(cnt)

def compare(a:str, b:str) -> bool:
    if len(a) != len(b):
        return False
    index = 0
    while index < len(a):
        if a[index] == b[index]:
            index += 1
        elif b[index] == '*':
            index += 1
        else:
            return False
    return True
#print(solution( ["frido", "frodo"],["fr*do", "fr**o"]))