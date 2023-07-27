class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        memo = defaultdict(int)
        for num in arr:
            memo[num] = 1 + memo[num - difference]
        
        return max(memo.values())
        

        
