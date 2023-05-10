class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        answer = []

        def findCycle(node, colors):
            nonlocal answer
            if colors[node] == 2:
                return False
            
            if colors[node] == 1:
                return True

            colors[node] = 1
            for neighbour in graph[node]:
                hasCycle = findCycle(neighbour, colors)
                if hasCycle == True:
                    return True
            colors[node] = 2
            answer.append(node)

            return False

        colors = [0] * len(graph)
        for i in range(len(graph)):
            if colors[i] == 0:
                findCycle(i, colors)
        
        return sorted(answer)
        
        
        



        
