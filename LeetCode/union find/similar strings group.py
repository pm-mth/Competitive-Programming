class Solution:

    def find(self, a):
        if self.rep[a] == a:
            return a
        
        root = self.rep[a]
        while root != self.rep[root]:
            root = self.rep[root]
        
        while  a != self.rep[a]:
            parent = self.rep[a]
            self.rep[a] = root
            a = parent
        
        return root
    
    def union(self, a, b):
        nodeA = self.find(a)
        nodeB = self.find(b)

        if nodeA != nodeB:
            if self.size[nodeA] < self.size[nodeB]:
                self.rep[nodeA] = self.rep[nodeB]
                self.size[nodeB] += self.size[nodeA]
            else:
                self.rep[nodeB] = self.rep[nodeA]
                self.size[nodeA] += self.size[nodeB]


    def numSimilarGroups(self, strs: List[str]) -> int:
        self.rep = {i:i for i in range(len(strs))}
        self.size = [1] * len(strs)

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                count = 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        count += 1
                    if count > 2:
                        break
              
                if count <= 2:
                    self.union(i, j)
        
        roots = set()
        for i in range(len(strs)):
            roots.add(self.find(i))
        return len(roots)
    
        
