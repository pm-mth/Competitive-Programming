class Solution:
    def reverseWords(self, s: str) -> str:
        newList = s.split()
        n = len(newList) - 1
        newS = ""
        for i in range(n,-1,-1):
            newS = newS + newList[i] +" "
        return newS[:-1]
            
            
