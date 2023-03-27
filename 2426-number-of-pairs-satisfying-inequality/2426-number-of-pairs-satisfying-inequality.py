class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.count = 0
        self.diff = diff
        nums = []
        for i in range(len(nums1)):
            nums.append(nums1[i] - nums2[i])
            
        self.divide(0, len(nums1), nums)
        
        return self.count
            
            
    
    def divide(self, l, r, nums):
        if l + 1 == r:
            return [nums[l]]
        
        mid = l + (r - l)//2
        left = self.divide(l, mid, nums)
        right = self.divide(mid, r, nums)
        
        return self.conquer(left, right)
    def conquer(self, left, right):
        p1, p2 = 0, 0
        acc = 0
        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2] + self.diff:
                acc += 1
                p1 += 1
            else:
                self.count += acc
                p2 += 1
        for _ in range(p2, len(right)):
            self.count += acc
        
        p1, p2 = 0, 0
        merge = []
        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2]:
                merge.append(left[p1])
                p1 += 1
            else:
                merge.append(right[p2])
                p2 += 1
        merge.extend(left[p1:])
        merge.extend(right[p2:])
        
        return merge
    
    
    
                
        