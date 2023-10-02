class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for ch in key:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.val = val
        

    def sum(self, prefix: str) -> int:
        
        @cache
        def dfs(cur):
            if not cur.children:
                return cur.val
            
            count = 0
            for key in cur.children:
                count += dfs(cur.children[key])
            if cur.val:
                count += cur.val
            
            return count
       

        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]   
        return dfs(cur)
        



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
