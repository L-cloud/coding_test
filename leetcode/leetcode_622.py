class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0]*k
        self.space = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.space -= 1
        if self.front == -1 :
            self.front = (self.front + 1) % len(self.q)
        self.rear = (self.rear + 1) % len(self.q)
        self.q[self.rear] = value
        return True

        
    def deQueue(self) -> bool:   
        if self.isEmpty():
            return False
        self.space += 1
        self.front = (self.front+1) % len(self.q)
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]
       
    def isEmpty(self) -> bool:
        return self.space == len(self.q)
        
    def isFull(self) -> bool:
        return self.space == 0
