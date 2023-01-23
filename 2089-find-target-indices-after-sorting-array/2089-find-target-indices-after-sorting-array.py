class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        target_indices = []
        for i in range(len(nums)):
            if nums[i] == target:
                target_indices.append(i)
        return target_indices
                
        