class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        colors = [0] * numCourses

        for suf, pre in prerequisites:
            graph[pre].append(suf)
        
        def findCourse(node, colors):
            if colors[node] == 2:
                return False
            
            if colors[node] == 1:
                return True
            
            colors[node] = 1
            for neighbour in graph[node]:
                if findCourse(neighbour, colors):
                    return True
            colors[node] = 2

            return False
        
        for i in range(numCourses):
            if colors[i] == 0:
                if findCourse(i, colors):
                    return False
        return True
