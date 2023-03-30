class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        used = 0
        def findPermute(cur):
            nonlocal used
            if len(cur) == len(nums):
                answer.append(cur.copy())
                return 
            
            for i in range(len(nums)):
                if used & (1 << i) == 0:
                    used |= (1 << i)
                    cur.append(nums[i])
                    findPermute(cur)
                    cur.pop()
                    used ^= (1 << i)
        findPermute([])
        return answer
                    
        
        