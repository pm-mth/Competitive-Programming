class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
#         counting the vote for every vote cast
        self.count = defaultdict(int)
        self.count[self.persons[0]] = 1 
        self.leading = [self.persons[0]]
        
        for p in self.persons[1:]:
            self.count[p] += 1
            
            if self.count[p] >= self.count[self.leading[-1]]:
                self.leading.append(p)
            else:
                self.leading.append(self.leading[-1])
       

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        answer = left
        while left <= right:
            mid =left + (right - left)//2
            
            if self.times[mid] > t:
                right = mid - 1
            else:
                answer = max(answer, mid)
                left = mid + 1
        return self.leading[answer]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
