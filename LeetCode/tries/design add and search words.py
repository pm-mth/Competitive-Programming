class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
        
            cur = cur.children[ch]
        cur.isWord = True 
                   
    def dfs(self, i, cur, ch):
        if i >=  len(ch):
            if cur.isWord:
                return True
            else:
                return False

        if ch[i] not in cur.children and ch[i] != ".":
            return False
        if ch[i] == ".":
            for key in cur.children:
                if self.dfs(i+ 1, cur.children[key], ch):
                    return True
            return False
        
        return self.dfs(i + 1, cur.children[ch[i]], ch)
                

    def search(self, word: str) -> bool:
        cur = self.root
        return self.dfs(0, cur, word)

        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
