def solution(numbers, target):
    sol = [0]
    def dfs(tempt, index):
        if len(tempt) == len(numbers):
            if sum(tempt) == target:
                sol[0] += 1
            return
        tempt.append(numbers[index])
        dfs(tempt,index +1)
        tempt.pop()
        tempt.append(-numbers[index])
        dfs(tempt,index + 1)
        tempt.pop()
    dfs([],0)
    return sol[0]


