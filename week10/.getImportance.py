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
        
        dic = {employee.id: employee for employee in employees}
        
        def find(ID):
            
            employee = dic[ID]
            if employee.subordinates == []:
                return employee.importance
            total = 0
            for sub in employee.subordinates:
                total += find(sub) 
            return employee.importance + total
        
        return find(id)
                
               
