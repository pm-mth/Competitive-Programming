class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = [-1]*len(nums1)
        dicts = defaultdict(int)
        for i in range(len(nums1)):
            dicts[nums1[i]] = i
        
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                indx = dicts[val]
                result[indx] = nums2[i]
                
            if nums2[i] in dicts:
                stack.append(nums2[i])
                
                    
            # for j in range(i+1, len(nums2)):
            #     if nums2[j] > nums2[i]:
            #         indx = dicts[nums2[i]]
            #         result[indx] = nums2[j]
            #         break
                
        return result
                    
                
        
