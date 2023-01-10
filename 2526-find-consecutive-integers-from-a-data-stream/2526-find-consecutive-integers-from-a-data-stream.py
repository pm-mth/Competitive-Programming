class DataStream:

    def __init__(self, value: int, k: int):
        self.DataStream = []
        self.value = value
        self.k = k
        self.diff_value_ptr = -1
        

    def consec(self, num: int) -> bool:
        self.DataStream.append(num)
        length = len(self.DataStream)
        
        if num != self.value:
            self.diff_value_ptr = length 

        if length < self.k:
            return False
      
        if self.diff_value_ptr == -1:
            return True 
        
        if (length - self.diff_value_ptr) < self.k :
            return False

        return True
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)