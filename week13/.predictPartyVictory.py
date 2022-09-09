class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()
        n = len(senate)
        for i in range (len(senate)):
            if senate[i] == "R":
                R.append(i)
            else:
                D.append(i)
                
        while R and D:
            Ridx = R.popleft()
            Didx = D.popleft()
            if Ridx < Didx:
                R.append(Ridx+n)
            else:
                D.append(Didx+n)
                
        if R:
            return "Radiant"
        else:
            return "Dire"
