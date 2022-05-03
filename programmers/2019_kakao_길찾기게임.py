from typing import List
import collections

def solution(nodeinfo:List[int]) -> List[int]:
    graph = {}
    for i,v in enumerate(nodeinfo, 1):
        graph[(v[0], v[1])] = i # tuple로 받음
    nodeinfo.sort(key = lambda x:(-x[1],x[0]), reverse = True) # y 값 크고 x값 작은 순
    level_graph = collections.defaultdict(list)
    level,prev = 0,nodeinfo[-1][1] # 가장 큰 y값 prev
    
    while nodeinfo: # 레벨별로 넣기
        node = nodeinfo.pop()
        N = Node(graph[(node[0], node[1])], node)
        if node[1] != prev: #
            level += 1
            prev = node[1]
        level_graph[level].append(N)
    
    parent, child = 0, 1
    while child <= level:
        index = 0
        for p in level_graph[parent]:
            index1 = index
            for c in level_graph[child][index1:index1 + 2]:
                if not p.left and c.coordinate[0] < p.coordinate[0]:
                    if p.left_min:
                        if  p.left_min < c.coordinate[0]: # p.left_min 있고 이거보다 큼
                            c.right_max = p.coordinate[0]
                            c.parent = p
                            c.left_min = p.left_min
                            p.left = c
                            index += 1     
                    else: # p.left_min 없음
                        c.right_max = p.coordinate[0]
                        c.parent = p
                        p.left = c
                        c.left_min = p.left_min
                        index += 1
                elif not p.right and p.coordinate[0] < c.coordinate[0]: # 오른쪽
                    if p.right_max:
                        if  c.coordinate[0] < p.right_max:
                            c.left_min = p.coordinate[0]
                            c.right_max = p.right_max
                            c.parent = p
                            p.right = c
                            index += 1
                    else:
                        c.left_min = p.coordinate[0]
                        c.right_max = p.right_max
                        c.parent = p
                        p.right = c
                        index += 1
        parent += 1
        child += 1


    answer = [[],[]]
    def pre(N:Node):
        if not N:
            return
        answer[0].append(N.index)
        pre(N.left)
        pre(N.right)

    def post(N:Node):
        if not N:
            return
        post(N.left)
        post(N.right)
        answer[1].append(N.index)
    pre(level_graph[0][0])
    post(level_graph[0][0])
    return answer

class Node: # 전위 후위 돌면서 prev.index append 해주면됨
    def __init__(self,index:int,coordinate:List[int]) -> None:
        self.parent = None
        self.left = None
        self.right = None
        self.index = index
        self.left_min = None
        self.right_max = None
        self.coordinate = coordinate
    


print(solution([[0,1],[2,2]]))
