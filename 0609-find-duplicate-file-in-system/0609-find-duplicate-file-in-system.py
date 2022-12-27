class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        count_duplicates = defaultdict(list)
        
        for s in paths:
            
            directories = s.split()
            
            for i in range(1,len(directories)):
                file_path = "/".join([directories[0],directories[i]])
                first, last = file_path.split("(")
                count_duplicates[last].append(first)
                
                
        ans = []
        for val in count_duplicates.values():
            if len(val) > 1:
                ans.append(val)
        return ans
                
            
        