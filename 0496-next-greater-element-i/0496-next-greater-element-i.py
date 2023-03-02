class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater_element = defaultdict(lambda: -1)
        
        for num in nums2:
            while stack and stack[-1] < num:
                greater_element[stack[-1]] = num
                stack.pop()
            
            stack.append(num)
        
        return [greater_element[num] for num in nums1]
        
        