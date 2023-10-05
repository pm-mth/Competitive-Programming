class Solution:
    def knightDialer(self, n: int) -> int:
        graph = defaultdict(list)
        edges = ["04", "06", "16", "18", "27", "29", "34", "38", "40", "43", "49", "60", "61", "67", "72", "76", "81", "83", "92", "94"]
        for s in edges:
            graph[int(s[0])].append(int(s[1]))


        @cache
        def dp(node, i):
            if i == n:
                return 1
            
            count = 0
            for neighbour in graph[node]:
                count += dp(neighbour, i + 1)

            return count
        res  = 0
        for i in range(10):
            res += dp(i, 1)
        return res % (10**9 + 7)

            


        
