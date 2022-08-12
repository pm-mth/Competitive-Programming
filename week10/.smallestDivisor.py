class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left, right = 1, max(nums)
        answer = max(nums)
        while left <= right:
            mid = left + (right - left)//2
            total = 0
            for num in nums:
                total += ceil(num/mid)
                
            if total > threshold:
                left = mid + 1
                
            elif total <= threshold:
                answer = min(answer, mid)
                right = mid - 1
                
        return answer
                    
