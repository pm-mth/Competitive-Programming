class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.stones = stones
        n = len(stones)
        self.rep = {i: i for i in range(n)}
        self.largest = [1] * n
        self.size = [0] * n
        answer = 0
  

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    print(i,j)
                    self.union(i, j)

        for i in range(n):
            if self.largest[i] > 1:
                answer += self.largest[i] - 1
        
        return answer
    
    def findRep(self, a):
        if a == self.rep[a]:
            return a
        
        parent = self.findRep(self.rep[a])
        self.rep[a] = parent

        return parent
    
    def union(self, a, b):
        nodeA = self.findRep(a)
        nodeB = self.findRep(b)
        if nodeA != nodeB:
            if self.size[nodeA] > self.size[nodeB]:
                self.rep[nodeB] = self.rep[nodeA]
                self.largest[nodeA] += self.largest[nodeB]
                self.largest[nodeB] = 1
                
            elif self.size[nodeB] > self.size[nodeA]:
                self.rep[nodeA] = self.rep[nodeB]
                self.largest[nodeB] += self.largest[nodeA]
                self.largest[nodeA] = 1
            else:
                self.rep[nodeA] = self.rep[nodeB]
                self.largest[nodeB] += self.largest[nodeA]
                self.largest[nodeA] = 1
                self.size[nodeB] += 1



