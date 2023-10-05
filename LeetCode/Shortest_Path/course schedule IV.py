class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        answer = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for i, j in prerequisites:
            answer[i][j] = True

        for i in range(numCourses):
            answer[i][i] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if answer[i][k] and answer[k][j]:
                        answer[i][j] = answer[i][k] and answer[k][j]
        
        res = []
        for i, j in queries:
            res.append(answer[i][j])
        return res
            
