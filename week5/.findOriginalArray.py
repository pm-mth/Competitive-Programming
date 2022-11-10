class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        count = defaultdict(int)
        result = []
        
        changed.sort()
        
        for num in changed:
            count[num] += 1
        
        for i in range(0, len(changed)):
            double = 2*changed[i]
            if changed[i] == 0 and  count[changed[i]] == 1 :
                continue
            #     result.append(changed[i])
            #     count[changed[i]] -= 1
            #     count[double] -= 1
                
            elif count[changed[i]] > 0 and double in count:
                if count[double] > 0:
                    result.append(changed[i])
                    count[changed[i]] -= 1
                    count[double] -= 1
            
            
        if len(changed) == 2*len(result):
            return result
        else:
            return []
            
