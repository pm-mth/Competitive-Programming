class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        count = Counter(nums)
        answer = []
        
        def findPermute(cur):
            if len(cur) == len(nums):
                answer.append(deepcopy(cur))
                return 
            
            for i in range(len(nums)):
                if count[nums[i]] != 0:
                    cur.append(nums[i])
                    count[nums[i]] -= 1
                    findPermute(cur)
                    count[nums[i]] += 1
                    cur.pop()
        findPermute([])
        return answer
                    
        
        