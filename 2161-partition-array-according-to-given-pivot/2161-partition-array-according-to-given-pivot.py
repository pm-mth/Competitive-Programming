class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        before_pivot = []
        in_between = []
        after_pivot = []
        for num in nums:
            if num < pivot:
                before_pivot.append(num)
            elif num == pivot:
                in_between.append(num)
            else:
                after_pivot.append(num)
                
        return before_pivot + in_between + after_pivot