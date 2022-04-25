def solution(board, moves):
    stack = []
    answer = 0
    for move in moves:
        i = 0
        while i < len(board) and board[i][move -1] == 0:
            i += 1
        if i < len(board):
            stack.append(board[i][move -1])
            board[i][move -1] = 0 
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))