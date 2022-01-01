def solution(n, costs):
    costs.sort(key = lambda x : x[2], reverse = True)
    routes = []
    solve = 0
    while costs:
        src, dst, cost = costs.pop()
        if not routes: # routes == []
            solve += cost
            routes.append({src, dst})
        else:
            cnt, union, is_break = 2, [], False
            for route in routes:
                if src in route and dst in route:
                    is_break = True
                    break # 이미 루트 존재
                elif src in route or dst in route: # 둘 중 하나만 연결
                    cnt -= 1
                    union.append(route)
                if cnt == 0:
                    break # 두 개 연결 된 것 찾았으니 그만 돌려도 됨
            if not is_break:
                solve += cost # for문 다 끝났으면 어찌되었는 cost + 해야함. 루트 존재하면 break 으로 끝냈을 터이니
                if cnt == 2: # 어디에도 연결x
                    routes.append({src, dst})
                elif cnt == 1:
                    union[0].add(src) # 어짜피 set()자체가 레퍼런스라서 이렇게 해도 됨 포인터 같은거라
                    union[0].add(dst)
                else : # cnt == 0 연결 해야함
                    route = union[0] | union[1] # 합집합
                    routes.remove(union[0]) # 기존 것 제거
                    routes.remove(union[1]) # 기존 꺼 제거
                    routes.append(route)
                for route in routes:
                    if len(route) == n:
                        return solve

# Better solution
# def solution(n, costs):
#     answer = 0
#     costs.sort(key=lambda x: x[2])  # 비용기준으로 오름차순 정렬
#     connect = set([costs[0][0]])  # 연결을 확인하는 집합
#
#     # Kruskal 알고리즘으로 최소 비용 구하기
#     while len(connect) != n:
#         for cost in costs:
#             if cost[0] in connect and cost[1] in connect:
#                 continue
#             if cost[0] in connect or cost[1] in connect:
#                 connect.update([cost[0], cost[1]])
#                 answer += cost[2]
#                 break
#
#     return answer
