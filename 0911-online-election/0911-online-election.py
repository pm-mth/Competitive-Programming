class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times     
        prefix = defaultdict(int)
        self.persons = persons
        
        self.winners = []
        recent = []
        max_val = 0
        
        for i in range(len(self.persons)):
            prefix[self.persons[i]] += 1
            if prefix[self.persons[i]] >= max_val:
                max_val = prefix[self.persons[i]]
                recent.append(self.persons[i])
            
            self.winners.append(recent[-1])
        
            
            
        
        
    def q(self, t: int) -> int:
        
        left, right = -1, len(self.times)
       
        
        while right > left + 1:
            mid = left + (right - left)//2
            
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid
                
        return self.winners[left]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)