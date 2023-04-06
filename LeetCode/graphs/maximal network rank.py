class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        self.graph = defaultdict(set)
        for i in range(len(roads)):
            self.addEdge(roads[i][0], roads[i][1])

        max_network = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans = len(self.graph[i]) + len(self.graph[j]) 
                if i in self.graph[j]:
                    ans -=  1
                max_network = max(max_network, ans)
        return max_network


    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)
