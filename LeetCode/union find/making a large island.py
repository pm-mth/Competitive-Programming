class Solution:
    def find(self, a):
        if a not in self.rep:
            self.rep[a] = a
            self.size[a] = 1
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
        nodeA = self.find(a)
        nodeB = self.find(b)
        

        if nodeA != nodeB:
            if self.size[nodeA] < self.size[nodeB]:
                self.rep[nodeA] = self.rep[nodeB]
                self.size[nodeB] += self.size[nodeA]
                
            else:
                self.rep[nodeB] = self.rep[nodeA]
                self.size[nodeA] += self.size[nodeB]

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.rep = {}
        directions = [(0,1), (1,0),(-1,0),(0,-1)]
        self.size = defaultdict(int)
        max_island = 0

        def inrange(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid)
        for i in range(len(grid)):
            for j in range(len(grid)):
                for r, c in directions:
                    if grid[i][j] == 1 and inrange(i+r, j +c) and grid[i+ r][j+c] == 1:
                        self.union((i+r, j+c), (i, j))
                        node = self.find((i, j))
                        max_island = max(max_island, self.size[node])

                
        
        
        
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                neighbours = set()
                island = 0
                for r, c in directions:
                    if grid[i][j] == 0 and inrange(i+r, j +c) and grid[i+ r][j+c] == 1:
                        node = self.find((i+r, j+c))
                        if node not in neighbours:
                            island += self.size[node]
                            neighbours.add(node)
                max_island = max(max_island, island + 1 )
        
        return max_island



