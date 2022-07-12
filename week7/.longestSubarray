class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        end = 0
        maxlen = 0

        windows = {}
        
        for end in range(len(nums)):
            if nums[end] in windows:
                windows[nums[end]] += 1
            else:
                windows[nums[end]] = 1
            
            mini = min(list(windows.keys()))
            maxi = max(list(windows.keys()))
            
            if maxi - mini <= limit:
                if maxlen < (end - start +1):
                    maxlen = end - start +1
                    
            
            else:
                while start < end:
                    windows[nums[start]] -= 1
                    
                    if windows[nums[start]] == 0:
                        windows.pop(nums[start])
                        
                    start += 1
                    
                    mini = min(list(windows.keys()))
                    maxi = max(list(windows.keys()))
                    
                    if maxi - mini <= limit:
                        break
        return maxlen
                        
                    
                
                
             
            
