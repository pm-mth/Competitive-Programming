from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		   
		def findCycle(node, colors,prev):
		    if colors[node] == 2:
		        return False
		    if prev != node and colors[node] == 1:
		        return True
		    
		    colors[node] = 1
		   
		    for neighbour in adj[node]:
		        if neighbour == prev:
		            continue
		        hasCycle = findCycle(neighbour, colors, node)
		        if hasCycle:
		            return True
		            
		    colors[node] = 2
		    
		    return False
		colors = [0] * V
		
		for i in range(V):
		    if colors[i] == 0:
		        hasCycle = findCycle(i, colors,i )
		
		        if hasCycle:
		            
		            return 1
		return 0
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
