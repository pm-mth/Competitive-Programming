class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.rep = {i:i for i in range(n)}
        self.size = [0] * n

        for u, v in edges:
            self.union(u, v)
            self.union(v, u)
        # print(self.rep)
        if self.findRep(source) is self.findRep(destination):
            return True
        return False
    
    def findRep(self, x):
        root = self.rep[x]
        while root != self.rep[root]:
            root = self.rep[root]
        
        while x != root:
            parent = self.rep[x]
            self.rep[x] = root
            x = parent
        
        return root
    
    def union(self, x, y):
        xrep = self.findRep(x)
        yrep = self.findRep(y)

        if xrep != yrep:
            lx, ly = self.size[xrep], self.size[yrep]
            if lx > ly:
                self.rep[yrep] = xrep
            elif ly > lx:
                self.rep[xrep] = yrep
            else:
                self.rep[xrep] = yrep
                self.size[yrep] += 1
            
