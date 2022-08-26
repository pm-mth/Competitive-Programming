class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = defaultdict(int)
        added  = defaultdict(bool)
        for i in s:
            count[i] += 1
        prev = [] #stack
        for i in s:
            count[i] -= 1
            if added[i] == True:
                continue
            while prev and prev[-1] > i and count[prev[-1]] > 0:
                added[prev[-1]] = False
                prev.pop() 
            if added[i] == False:
                added[i] =True
                prev.append(i)
        return "".join(prev)
