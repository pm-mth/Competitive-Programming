class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         time complexity = n*m**2
#         space complexity = n
        
        
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        
        nei = defaultdict(list)
        wordList.append(beginWord)
#         creating graph data structure
        for word in wordList:
            for i in range(n):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
# traversing by BFS
        q = collections.deque()
        q.append(beginWord)
        visited = set([beginWord])
        dist = 0
        while q:
            dist += 1 
            for _ in range(len(q)):
                current = q.popleft()
                if current == endWord:
                    return dist
                for i in range(n):
                    pattern = current[:i] + "*" + current[i+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
        
        return 0                
                    
                
    
