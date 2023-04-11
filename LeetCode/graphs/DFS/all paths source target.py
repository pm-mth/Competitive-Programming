class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.answer = []
        self.searchPath(0, [0])
        return self.answer

    
    def searchPath(self,vertex, inter):
        if vertex == len(self.graph) - 1:
            self.answer.append(inter.copy())
            return
        
        for num in self.graph[vertex]:
            inter.append(num)
            self.searchPath(num, inter)
            inter.pop()
    
        
