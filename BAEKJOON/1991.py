import sys
N = int(sys.stdin.readline())
graph = {}
# 노드 이름은 A로 시작
for _ in range(N):
    parent, left, right = map(str,sys.stdin.readline().split())
    graph[parent] = [left, right]

def prefix(node:str) -> None:
    if node == '.':
        return
    print(node, end='')
    prefix(graph[node][0])
    prefix(graph[node][1])

def infix(node:str) -> None: 
    if node == '.':
        return
    infix(graph[node][0])
    print(node, end='')
    infix(graph[node][1])

def postfix(node:str)-> None:
    if node == '.':
        return
    postfix(graph[node][0])
    postfix(graph[node][1])
    print(node, end='')


prefix('A')
print()
infix('A')
print()
postfix('A')
