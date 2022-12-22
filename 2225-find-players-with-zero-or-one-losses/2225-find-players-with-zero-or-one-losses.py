class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        #add the first element of the list to a set
        winners = set()
        for i in range(len(matches)):
            winners.add(matches[i][0])
            
        #add the second element to hashmap
        losers = defaultdict(int)
        for i in range(len(matches)):
            losers[matches[i][1]] += 1
        
        #find list of players who have not lost any match
        lost_none = []
        for num in winners:
            if num not in losers.keys():
                lost_none.append(num)
        
        #find list of players who have lost exactly one match
        lost_one = []
        for key in losers.keys():
            if losers[key] == 1:
                lost_one.append(key)
                
        #sort the answers
        lost_one.sort()
        lost_none.sort()
        
        #final answer
        return [lost_none, lost_one]
        
            
        
        