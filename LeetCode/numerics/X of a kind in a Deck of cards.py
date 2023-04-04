class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        ans = set(count.values())
        min_val = min(ans)
        for num in ans:
            min_val = self.gcd(min_val, num)
            if min_val == 1:
                return False
        return True
            

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
        
