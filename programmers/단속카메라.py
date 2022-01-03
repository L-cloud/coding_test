def solution(routes):
    routes.sort(key = lambda  x :(x[0], -x[1]))  # 가장 늦게 출발 하면서 가장 빨리 도착하는 순
    answer = 1
    intersection = range(routes[0][0], routes[0][1] + 1)
    for route in routes:
        intersection = range(max(intersection[0],route[0]), min(intersection[-1], route[-1]) + 1)
        if not intersection:
            answer += 1
            intersection = range(route[0], route[1] + 1)
    return answer
