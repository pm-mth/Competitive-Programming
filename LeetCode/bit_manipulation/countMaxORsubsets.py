class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.nums = nums
        self.maxOR = 0
        self.answer = []
        count = 0
        self.subsets(0, [])
        for i in range(len(self.answer)):
            if self.answer[i] == self.maxOR:
                count += 1
        return count

    
    def subsets(self, i, inter):
        if i == len(self.nums):
            ans = self.bitwiseOR(inter)
            self.maxOR = max(self.maxOR, ans)
            self.answer.append(ans)
            return 
        
        inter.append(self.nums[i])
        self.subsets(i + 1 , inter)
        inter.pop()
        self.subsets(i + 1, inter)
        
    def bitwiseOR(self, inter):
        if not inter:
            return 0
        acc = 0
        for num in inter:
            acc |= num
        return acc
