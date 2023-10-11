# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList =nestedList
        self.i = 0
        self.flattened = self.find(self.nestedList)


    def find(self, arr):
        j = 0
        m = len(arr)
        flattened = []
        while j < m:
            if arr[j].isInteger():
                flattened.append(arr[j].getInteger())
            else:
                newList = arr[j].getList()
                flattened.extend(self.find(newList))
            j += 1
        return flattened

        
        
      
    def next(self) -> int:
        self.i += 1
        return self.flattened[self.i - 1]
        
       
        
    
    def hasNext(self) -> bool:
        return self.i < len(self.flattened)
          

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
