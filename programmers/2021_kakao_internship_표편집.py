
from typing import List 

def solution(n:int, k:int, cmd :List[str]) -> str :  # n-> 배열 갯수, k 처음 선택된 행의 위치
    exel = Exel(None, n)
    prev = None
    for i in range(n):
        node = Node(i,prev)
        if i == 0 : # 처음이면
            exel.root = node
        if i == k: # 현재임
            exel.current = node
        if prev:
            prev.connect[1] = node
            prev.next_for_return = node
        prev = node
    for c in cmd:
        command = c.split()
        if command[0] == 'D':
            exel.down(int(command[1]))
        elif command[0] == 'U':
            exel.up(int(command[1]))
        elif command[0] == 'C':
            exel.remove()
        else : # Z
            exel.ctrlz()
    return ''.join(exel.answer)

class Node:
    def __init__(self,index:int, prev) -> None:
        self.index = index
        self.connect = [prev, None]
class Exel:
    def __init__(self, root:Node, N:int) -> None:
        self.root = root
        self.current = None
        self.answer = ['O' for i in range(N)]
        self.q = []
    
    def down(self,index:int) -> None:
        print("Before down", self.current.index, end = " ")
        for _ in range(index):
            self.current = self.current.connect[1]
        print("Aefore up", self.current.index)  

    
    def up(self, index :int) -> None:
        print("Before up", self.current.index, end = " ")
        for _ in range(index):
            self.current = self.current.connect[0] 
        print("Aefore up", self.current.index)   
    
    def remove(self) -> None:
        node = self.current
        print("remove : node =", node.index)
        if node.connect[1]:
            self.current = node.connect[1]
            self.current.connect[0] = node.connect[0]
        else: # 마지막
            self.current = node.connect[0]
            if self.current:
                self.current.connect[1] = None
        if self.current and self.current.connect[0]: # 이전이 있다면
            self.current.connect[0].connect[1] = self.current
        self.answer[node.index] = 'X'
        print("Before remove", node.index,"After remove", self.current.index)
        self.q.append(node)


    def ctrlz(self) -> None:
        node = self.q.pop()
        prev_ = node.connect[0]
        next_ = node.connect[1]
        # while prev_: # 첫 번째인 경우도 생각해야함
        #     if self.answer[prev_.index] == 'O': # 제거 안 됨
        #         break
        #     else: #이미 제거됨
        #         prev_= prev_.prev_for_return 
        
        # while next_:
        #     if self.answer[next_.index] == 'O': #제거 안 됨
        #         break
        #     else:
        #         next_ = next_.next_for_return
        
        if prev_:
            prev_.connect[1] = node
        if next_:
            next_.connect[0] = node
        node.connect[1] = next_
        node.connect[0] = prev_
        self.answer[node.index] = 'O'
        print('pop = ', node.index)

print(solution(4,0,["C","Z","C","Z",'D 1',"C","Z","C","C"]))