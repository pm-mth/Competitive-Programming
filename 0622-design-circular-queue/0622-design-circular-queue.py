class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque()
        self.k = k
        
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        
        return True 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.popleft()
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[0]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[-1]
        

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if len(self.queue) == self.k:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()