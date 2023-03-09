class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        count = Counter(nums)
        answer = []
        nums.sort()
        
        def findPermute(cur):
            if len(cur) == len(nums):
                answer.append(deepcopy(cur))
                return 
            i = 0
            while i  < len(nums):
                if count[nums[i]] != 0:
                    cur.append(nums[i])
                    count[nums[i]] -= 1
                    findPermute(cur)
                    count[nums[i]] += 1
                    cur.pop()
                while i + 1 < len(nums) and nums[i ] == nums[i + 1]:
                    i += 1
                i += 1
                    
        findPermute([])
        return answer
                    
        
        
        