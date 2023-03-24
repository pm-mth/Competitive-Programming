class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.answer = 0
        self.requests = requests
        count = defaultdict(int)
        self.findRequests(0, count, 0)
        return self.answer
    
    def findRequests(self, i, nums, acc):
        if i == len(self.requests):
            if self.check(nums):
                self.answer = max(self.answer, acc)
            return
        
        nums[self.requests[i][0]] += 1
        nums[self.requests[i][1]] -= 1
        self.findRequests(i + 1, nums, acc + 1)
            
        nums[self.requests[i][0]] -= 1
        nums[self.requests[i][1]] += 1
        self.findRequests(i+1, nums, acc)
            
    def check(self, count):
        for key in count.keys():
            if count[key] != 0:
                return False
        return True
            
                
            
        
       