class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.answer = 0
        self.divide(0, len(nums), nums)
        return self.answer
    
    def divide(self, l, r, nums):
        if l + 1 == r:
            return [nums[l]]
        
        mid = l + (r - l)//2
        left = self.divide(l, mid, nums)
        right = self.divide(mid, r, nums)
        return self.merge(left, right)
    def merge(self, left, right):
        p1, p2 = 0, 0
       
        while p1 < len(left) and p2 < len(right):
            if left[p1] > 2 * right[p2]:
                self.answer += (len(left) - p1) * 1
                p2 += 1
            else:
                p1 += 1 
        p1, p2 = 0, 0
        inter = []
        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2]:
                inter.append(left[p1])
                p1 += 1
            else:
                inter.append(right[p2])
                p2 += 1
                
        if p1 < len(left):  
            inter.extend(left[p1:])
        else:
            inter.extend(right[p2:])
        return inter
                
            
        
        
        
        