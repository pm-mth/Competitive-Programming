class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        
        left , max_size = 0, 0
        for right in range(len(nums)):
            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()
            
            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()
                
            min_queue.append(nums[right])
            max_queue.append(nums[right])
            
            
            
            while left < right and  abs(max_queue[0] -  min_queue[0]) > limit:
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                    
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                left += 1
                
            max_size = max(max_size, right - left + 1)
                    
        return max_size
                    
        
        