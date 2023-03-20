class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def backTrack(i = 0, unique = set()):
            nonlocal max_ans
            max_ans = max(max_ans, len(unique))
            if i == len(arr):
                return
            
            for j in range(i, len(arr)):
                temp = set()
                valid = True
                for char in arr[j]:
                    if char in unique or char in temp:
                        valid = False
                        break
                    temp.add(char)
                if not valid:
                    continue
                
                for char in temp:
                    unique.add(char)
                backTrack(j + 1, unique)
                for char in temp:
                    unique.remove(char)
            
        max_ans = 0
        backTrack()
        
        return max_ans