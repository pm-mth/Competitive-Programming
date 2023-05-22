class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz"
        self.rep = {i:i for i in range(len(s))}
        self.size = defaultdict(int)
        self.strings = defaultdict(list)
        self.index = defaultdict(list)

        for a, b in pairs:
            self.union(a, b)
        for i in range(len(s)):
            self.strings[self.findRep(i)].append(s[i])
            self.index[self.findRep(i)].append(i)
        
        answer = list(s)
        for key in self.strings:
            letters = sorted(self.strings[key])
            for idx, ele in enumerate(self.index[key]):
                answer[ele] = letters[idx]
        

        return "".join(answer) 
    
    def union(self, a, b):
        nodeA = self.findRep(a)
        nodeB = self.findRep(b)

        if nodeA != nodeB:
            if self.size[nodeA] > self.size[nodeB]:
                self.rep[nodeB] = self.rep[nodeA]
            elif self.size[nodeB] > self.size[nodeA]:
                self.rep[nodeA] = self.rep[nodeB]
            else:
                self.rep[nodeA] = self.rep[nodeB]
                self.size[nodeB] += 1
    
    def findRep(self, a):
        if self.rep[a] == a:
            return a
        
        parent = self.findRep(self.rep[a])
        self.rep[a] = parent

        return parent

     
        

        


    
