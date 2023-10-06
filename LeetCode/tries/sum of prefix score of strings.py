class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.val += 1
    
    def dfs(self, cur):
        if not cur.children:
            return cur.val 
        
        for ch in cur.children:
            cur.val += self.dfs(cur.children[ch])
    
        return cur.val
    
    def search(self, word):
        cur = self.root
        count = 0
        for ch in word:
            cur = cur.children[ch]
            count += cur.val
        
        return count
        
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert(word)
        
        self.dfs(self.root)

        res = []
        for word in words:
            res.append(self.search(word))
        
        return res
        
