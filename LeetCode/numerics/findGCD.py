class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        return self.gcd(max_val, min_val)
    
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
