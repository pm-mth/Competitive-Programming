class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.rep = {s:s for s in alphabets}
        self.size = {s:0 for s in alphabets}
        

        for equa in equations:
            a, b = equa[0], equa[3]
            if equa[1] == equa[2]:
                flag =True
            else:
                flag = False
            if not self.union(a, b , flag):
                return False
                
        for equa in equations:
            a, b = equa[0], equa[3]
            if equa[1] == equa[2]:
                flag =True
            else:
                flag = False
            if self.findRep(a) == self.findRep(b) and not flag:
                return False
        return True

    # def findRep(self, a):
    #     root = self.rep[a]
    #     while root != self.rep[root]:
    #         root = self.rep[root]
        
    #     while a != self.rep[a]:
    #         parent = self.rep[a]
    #         self.rep[a] = root
    #         a = parent
        
    #     return root
    
    def findRep(self, a):
        if a == self.rep[a]:
            return a
        
        parent = self.findRep(self.rep[a])
        self.rep[a] = parent

        return parent
    
    def union(self, a, b, flag):
        nodeA = self.findRep(a)
        nodeB = self.findRep(b)

        if not flag and nodeA == nodeB:
            return False
        if not flag and nodeA != nodeB:
            return True
        
        
        if self.size[nodeA] < self.size[nodeB]:
            self.rep[nodeB] = self.rep[nodeA]
        elif self.size[nodeB] < self.size[nodeA]:
            self.rep[nodeA] = self.rep[nodeB]
        else:
            self.rep[nodeA] = self.rep[nodeB]
            self.size[nodeB] += 1
        return True
