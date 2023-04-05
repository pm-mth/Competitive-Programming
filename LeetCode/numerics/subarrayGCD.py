class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] < k:
                continue
            ans = nums[i]
            for j in range(i, len(nums)):
                if nums[j] < k:
                    break
                ans = self.gcd(ans, nums[j])
                if ans < k:
                    break
                if ans == k:
                    count += 1

        return count

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

        
       
