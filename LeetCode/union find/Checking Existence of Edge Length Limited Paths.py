class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.rep = {i:i for i in range(n)}
        answer = [0] * len(queries)
        self.size = [0] * n
        edgeList.sort(key = lambda x:x[2])
        sortedQueries = [[v[0],v[1],v[2], i] for i, v in enumerate(queries)]
        sortedQueries.sort(key = lambda x:x[2])

        j = 0

        for i in range(len(sortedQueries)):
            u, v, w, idx = sortedQueries[i]

            while j < len(edgeList):
                x, y, z = edgeList[j]
                if z >= w:
                    break
                self.union(x, y)
                j += 1
            if self.findRep(u) == self.findRep(v):
                answer[idx] = True
            else:
                answer[idx] = False

        return answer
    

    def findRep(self, a):
        if self.rep[a] == a:
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
                
            elif self.size[nodeB] > self.size[nodeA]:
                self.rep[nodeA] = self.rep[nodeB]
                
            else:
                self.rep[nodeA] = self.rep[nodeB]
                self.size[nodeB] += 1
            
                
