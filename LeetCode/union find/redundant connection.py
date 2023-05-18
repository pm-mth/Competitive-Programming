class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.rep = {i:i for i in range(len(edges))}
        self.size = [0] * len(edges)
        self.answer = [0, 0]

        for a, b in edges:
            self.union(a - 1, b - 1)
        
        return self.answer

    
    def findRep(self, a):
        root = self.rep[a]
        while root != self.rep[root]:
            root = self.rep[root]
        
        while a != self.rep[a]:
            parent = self.rep[a]
            self.rep[a] = root
            a = parent
        
        return root

    
    def union(self, a, b):
        nodeA = self.findRep(a)
        nodeB = self.findRep(b)

        if nodeA == nodeB:
            self.answer = [a + 1, b + 1]
            return 
        
        if self.size[nodeA] > self.size[nodeB]:
            self.rep[nodeB] = self.rep[nodeA]
        elif self.size[nodeB] > self.size[nodeA]:
            self.rep[nodeA] = self.rep[nodeB]
        else:
            self.rep[nodeA] = self.rep[nodeB]
            self.size[nodeB] += 1
        
        return 
