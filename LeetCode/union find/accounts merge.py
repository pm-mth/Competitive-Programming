class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.rep = {i:i for i in range(len(accounts))}
        self.size = [0] * len(accounts)
        self.emails = defaultdict(set)
        visited = set()
        result = []
        for i in range(len(accounts)):
            self.emails[i].update(set(accounts[i][1:]))
        
        for i in range(len(accounts)):
            for j in range(i + 1, len(accounts)):
                common = self.emails[i].intersection(self.emails[j])
                if common:
                    self.union(i, j)
        
        for i in range(len(accounts)):
            ans = self.findRep(i)
            if ans not in visited:
                visited.add(ans)
                temp = [accounts[ans][0]] + sorted(self.emails[ans])
                result.append(temp)
        
        return result
    
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
                self.emails[nodeA].update(self.emails[nodeB])
            elif self.size[nodeB] > self.size[nodeA]:
                self.rep[nodeA] = self.rep[nodeB]
                self.emails[nodeB].update(self.emails[nodeA])
            else:
                self.rep[nodeA] = self.rep[nodeB]
                self.size[nodeB] += 1
                self.emails[nodeB].update(self.emails[nodeA])
            

        
