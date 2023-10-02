class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str) -> None:
        cur = self.root
        for ch in key:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
    
    @cache
    def dfs(self, cur, word):
        if not cur.children:
            return word
        
        mini = word
        for ch in cur.children:
            if cur.children[ch].is_end:
                temp = self.dfs(cur.children[ch], word + ch)
                print(temp, mini, ch)
                if len(temp) == len(mini):
                    mini = min(temp, mini)
                else:
                    if len(temp) > len(mini):
                        mini = temp
        return mini
            

    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.insert(word)
        
    
        return self.dfs(self.root, "")


        
