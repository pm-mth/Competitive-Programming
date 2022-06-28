class Solution:
    def sortSentence(self, s: str) -> str:
        lists=s.split()
        dic= defaultdict (int)
        for i in range(len(lists)):
            dic[int(lists[i][-1])]=lists[i][:-1]
            
        a=""
        for i in range(len(lists)):
            a += str(dic[i+1]) + " "
        a = a[:-1]    
        return a
