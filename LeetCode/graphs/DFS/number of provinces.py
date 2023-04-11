class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = defaultdict(list)
        for i in  range(len(isConnected)):
            cities[i].append(i)
            for j in range(i+1, len(isConnected[i])):
                if isConnected[i][j]== 1:
                    cities[i].append(j)
                    cities[j].append(i)

        visited = set()
        def dfs(vertex):

            visited.add(vertex)
            for node in cities[vertex]:
                if node not in visited:
                    dfs(node)
            return 1
        
        ans = 0
        for key in cities.keys():
            if key not in visited:
                ans += dfs(key)
        return ans
    
    
