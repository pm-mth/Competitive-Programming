class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for i in range(len(edges)):
            indegree[edges[i][1]] += 1
            outdegree[edges[i][0]] += 1
        source = []
        for i in range(n):
            if outdegree[i] >= 0 and indegree[i] == 0:
                source.append(i)
        return source
    
    
