class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.rep = {i: i for i in range(1, n + 1)}
        self.minimum = [float(inf)] * n
        
        for u, v, score in roads:
            self.union(u, v, score)
        
        return self.minimum[self.findRep(n) - 1]

    
    def findRep(self, a):
        root = self.rep[a]
        while root != self.rep[root]:
            root = self.rep[root]
        
        while a != self.rep[a]:
            parent = self.rep[a]
            self.rep[a] = root
            a = self.rep[a]
        
        return root
    
    def union(self, a, b, score):
        nodeA = self.findRep(a)
        nodeB = self.findRep(b)

        if nodeA != nodeB:
            if self.minimum[nodeA - 1] <= self.minimum[nodeB - 1]:
                self.rep[nodeB] = self.rep[nodeA]
                self.minimum[nodeA - 1] = min(self.minimum[nodeA -1], score)
            else:
                self.rep[nodeA] = self.rep[nodeB]
                self.minimum[nodeB - 1] = min(self.minimum[nodeB -1], score)
        else:
            self.minimum[nodeA - 1] = min(self.minimum[nodeA - 1], score)
                
               
       
