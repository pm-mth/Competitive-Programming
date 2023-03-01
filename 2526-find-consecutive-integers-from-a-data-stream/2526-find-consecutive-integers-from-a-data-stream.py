class DataStream:

    def __init__(self, value: int, k: int):
        self.dataStream = deque()
        self.value = value
        self.k = k
        self.track = 0
        
        
        

    def consec(self, num: int) -> bool:
        if len(self.dataStream) == self.k:
            self.dataStream.popleft()
            self.track -= 1 
            
        self.dataStream.append(num)
        
        if num != self.value:
            self.track = len(self.dataStream)
            
        if self.track <= 0 and len(self.dataStream) == self.k:
            return True
        
        return False
        
           
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)