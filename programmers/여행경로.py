import collections


def solution(tickets):
    route = collections.defaultdict(list)
    answer, num = ['ICN'], 0
    for scr, dst in tickets:
        route[scr].append(dst)
        num += 1
    for k in route.keys():
        route[k].sort()

    def dfs(route, answer, num):
        if num == 0:
            return True
        elif len(route[answer[-1]]) == 0:  # num != 0 and rout[next_scr] == []
            return False
        else:
            for index, node in enumerate(route[answer[-1]]):  # 지우고 복구 해야하는데 순서를 유지...
                route[answer[-1]].remove(node)
                answer.append(node)
                if dfs(route, answer, num - 1):
                    return True
                else:
                    answer.pop()
                    route[answer[-1]].insert(index, node)
            return False

    dfs(route, answer, num)

    return answer

solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]])