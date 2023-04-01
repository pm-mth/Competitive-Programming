class Solution:
    def maxProduct(self, words: List[str]) -> int:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        order = defaultdict(int)
        
        for i in range(len(alpha)):
            order[alpha[i]] = i
        
        track = defaultdict(int)
        for w in words:
            newS = set(w)
            mask = 0
            for s in newS:
                mask ^= 1 << order[s]
            track[w] = mask
        
        max_val = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (track[words[i]] & track[words[j]]):
                    max_val = max(max_val, len(words[i]) * len(words[j]))
        return max_val



        
