class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        for i in range(len(edges)):
            self.addEdges(edges[i][0], edges[i][1])
        n = len(self.graph)
        for key in self.graph.keys():
            if len(self.graph[key])  == n - 1:
                return key
    
    def addEdges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
