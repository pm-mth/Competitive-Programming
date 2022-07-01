class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        s = []
        check = []
        for i in range (len(l)):
            for j in range(l[i], r[i]+1):
                s.append(nums[j])
            s.sort()
            # print(s)
            for j in range(len(s)-1):
                if s[j+1]-s[j] == s[1]- s[0]:
                    check.append(True)
                else:
                    check.append(False)
            # print(check)
        
            if False in check:
                answer.append(False)
            else:
                answer.append(True)
            s = []
            check = []
            
        
        return answer
                    
                
 
