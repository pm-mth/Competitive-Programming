class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def solve(i):
            if i == 0:
                return nums[i]
            
            if i == 1:
                return max(nums[i], nums[i -1])


            if i not in memo:
                left = solve(i - 1)
                right = solve(i -2) + nums[i]

                memo[i] = max(left, right)
            
            return memo[i]
        
        memo = {}
        last = solve(n - 2)

        nums.reverse()
        memo =  {}
        first = solve( n - 2)
        return max(first, last)
            

