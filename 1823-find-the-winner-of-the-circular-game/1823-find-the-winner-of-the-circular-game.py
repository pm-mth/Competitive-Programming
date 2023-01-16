class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friend_circle = []
        for i in range(1, n+1):
            friend_circle.append(i)
            
        index = 0
        countedFriends = 1
        while len(friend_circle) > 1:
            if countedFriends == k:
                friend_circle.pop(index)
                countedFriends = 0
                index -= 1
                
            countedFriends += 1
            index = (index + 1) % len(friend_circle)
            
        return friend_circle[0]
                
            
            
            