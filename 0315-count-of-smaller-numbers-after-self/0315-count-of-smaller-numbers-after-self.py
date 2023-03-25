class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.nums = nums
        index = [i for i in range(len(nums))]
        arr = self.divide(0, len(index), index)
        answer = [0] * len(arr)
        for i in range(len(arr)):
            answer[arr[i][0]] = arr[i][1]
        return answer
            
        
    
    def divide(self, l, r, index):
        if l + 1 == r:
            return [[index[l], 0]]
        
        mid = l + (r - l)//2
        right = self.divide(mid, r, index)
        left = self.divide(l, mid, index)
        return self.merge(left, right)
    
    def merge(self, left, right):
        count = 0
        p1, p2 = 0, 0
        while p1 < len(left) and p2 < len(right):
            if self.nums[left[p1][0]] > self.nums[right[p2][0]]:
                count += 1
                p2 += 1
            else:
                left[p1][1] += count
                p1 += 1
                
        while p1 < len(left):
            left[p1][1] += count
            p1 += 1
            
        inter = []
        p1, p2 = 0, 0
        while p1 < len(left) and p2 < len(right):
            if self.nums[left[p1][0]] <= self.nums[right[p2][0]]:
                inter.append(left[p1])
                p1 += 1
            else:
                inter.append(right[p2])
                p2 += 1
                
        inter.extend(left[p1:])
        inter.extend(right[p2:])
            
        return inter
                
            
        
        
                
        
        