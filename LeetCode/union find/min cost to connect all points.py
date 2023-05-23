class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.rep = {i:i for i in range(len(points))}
        self.size = [0] * len(points)
        cost  = []
        self.minCost = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                calCost = abs(points[i][0] - points[j][0]) + abs(points[i][1]- points[j][1])
                cost.append((calCost, i, j))
        cost.sort()  
        for c, i, j in cost:
            self.union(i, j, c)

        return self.minCost
    def findRep(self, a):
        if self.rep[a] == a:
            return a
        parent = self.findRep(self.rep[a])
        self.rep[a] = parent

        return parent
    
    def union(self, a, b, cost):
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
            self.minCost += cost
                
            
