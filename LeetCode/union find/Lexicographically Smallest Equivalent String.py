class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.rep =  {s:s for s in s1 + s2}
        # print(self.rep)
        # self.size = {s: 0 for s in s1 + s2}
        for i in range(len(s1)):
            self.union(s1[i], s2[i])

        answer = ""
        for s in baseStr:
            answer += self.findRep(s)
        

        return answer
    
    def findRep(self, a):
        if a not in self.rep:
            return a

        root = self.rep[a]
        while root != self.rep[root]:
            root = self.rep[root]
        
        while a != self.rep[a]:
            parent = self.rep[a]
            self.rep[a] = root
            a = self.rep[a]
        
        return root
    
    def union(self, a, b):
        nodeA = self.findRep(a)
        nodeB = self.findRep(b)

        if nodeA != nodeB:
            if nodeA < nodeB:
                self.rep[nodeB] = self.rep[nodeA]
            else:
                self.rep[nodeA] = self.rep[nodeB]
        

