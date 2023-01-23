class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        maximum_coins = 0
        for i in range(n//3, n, 2):
            maximum_coins += piles[i]
        return maximum_coins
        