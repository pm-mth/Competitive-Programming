class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(dislikes)):
            graph[dislikes[i][0]].append(dislikes[i][1])
            graph[dislikes[i][1]].append(dislikes[i][0])
        
        colour = [-1] * n

        def dfs(vertex):
            for child in graph[vertex]:
                if colour[child - 1] != -1:
                    if colour[child - 1] == colour[vertex -1]:
                        return True
                    continue

                if colour[vertex - 1] == 1:
                    colour[child - 1] = 0
                else:
                    colour[child - 1] = 1
                if dfs(child):
                    return True
      
      
        for i in range(n):
            if colour[i] == -1:
                colour[i] = 1
                if dfs(i + 1):
                    return False
   
        return True

            

            
            
            
            
            
            
