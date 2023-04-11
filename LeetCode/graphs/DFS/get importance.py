"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict()
        for employee in employees:
            graph[employee.id] = employee

        def dfs(employee):
            if employee.subordinates == []:
                return employee.importance
            
            ans = 0
            for sub in employee.subordinates:
                ans += dfs(graph[sub])

            return ans + employee.importance
       
        return dfs(graph[id])
            

        
