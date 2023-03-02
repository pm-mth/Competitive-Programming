class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def solve(l, r, player1, player2, turn):
            #base case
            if l > r:
               
                return player1 >= player2
            
            
            #recurrence relation
            if turn:
                left = solve(l+1, r, player1 + nums[l], player2, not turn)
                right = solve(l, r-1, player1 + nums[r], player2, not turn)
                
             
                return left or right
            
            left = solve(l+1, r, player1, player2 + nums[l], not turn)
            right = solve(l, r-1, player1, player2 + nums[r], not  turn)
            
            return left and right 
        
        return solve(0, len(nums) - 1, 0, 0, True)
                
            
            
                