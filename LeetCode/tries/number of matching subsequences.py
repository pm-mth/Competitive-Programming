class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index = defaultdict(list)
        for i in range(len(s)):
            index[s[i]].append(i)
    
        def binarySearch(arr, num):
            l, r = -1, len(arr)

            while l + 1 < r :
                mid = l + (r - l)//2

                if arr[mid] < num:
                    l = mid 
                else:
                    r = mid
            
            return r
        count = 0

        for word in words:
            i = -1
            flag = True
            for ch in word:
                i = binarySearch(index[ch], i + 1)
                if i == len(index[ch]):
                    count -= 1
                    break
                i = index[ch][i]
                
            
            count += 1
        
        return count
                
            
         

        
