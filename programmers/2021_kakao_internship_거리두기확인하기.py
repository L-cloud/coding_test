from typing import List
def solution(places):
    answer = []
    for k in range(5):
        participants = find_participant(places[k])
        dx1 = [0,1,0,-1]
        dy1 = [1,0,-1,0] # 오른쪽부터 시계방향 대각선 맞추기 위해
        dxy = [[0,1],[1,0],[0,-1],[-1,0]] # 한 칸씩 늘리기 용도
        dx2 = [-1,1,1,-1] # 시계방향 대각선
        dy2 = [1,1,-1,-1]
        flag = True
        while participants and flag:
            row, col = participants.pop()
            for i in range(4):
                r = row + dx1[i]
                c = col + dy1[i]
                r2 = r + dxy[i][0]
                c2 = c + dxy[i][1] # 가로 세로 한 칸 늘린거
                r3 = row + dx2[i]
                c3 = col + dy2[i] # 대각선
                row_block = row + dx1[i -1]
                col_block = col + dy1[i - 1] # 대각선에서 파티션 있는지 없는지 확인용
                if 0<= r < 5 and 0<= c < 5: # 가로 세로 확인 
                    if places[k][r][c] == "X":
                        pass
                    elif places[k][r][c] == 'P' or ((0<= r2< 5 and 0<= c2 < 5) and  places[k][r2][c2] == 'P'):
                        answer.append(0)
                        flag = False
                        break
                if 0<= r3 < 5 and 0<= c3 < 5: # 대각선 확인
                    if places[k][r3][c3] == 'P': # 대각선에 사람 있음
                        if places[k][r][c] == 'X' and places[k][row_block][col_block] == 'X': # 대각선 위 아래 파티션으로 막힘
                            pass
                        else: # 벽으로 안 막힘
                            answer.append(0)
                            flag = False
                            break
        if flag:
            answer.append(1)
    return answer


def find_participant(place:List[str]):
    participants = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                participants.append([i,j])
    return participants