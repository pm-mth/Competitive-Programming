class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd = defaultdict(int)
        even = defaultdict(int)
        fmaxe, fmaxo, smaxe, smaxo = 0,0,0,0
        for i in range(len(nums)):
            if i % 2 == 0:
                even[nums[i]] += 1
            else:
                odd[nums[i]] += 1
               
        even_sort = sorted(list(even.items()), key = lambda x:x[1], reverse = True)
        odd_sort = sorted(list(odd.items()), key = lambda x :x[1], reverse = True)
        fmaxe = even_sort[0][0] if len(even_sort) > 0 else 0
        fmaxo = odd_sort[0][0] if len(odd_sort) > 0 else 0
        smaxe = even_sort[1][0] if len(even_sort) > 1 else 0
        smaxo = odd_sort[1][0] if len(odd_sort) > 1 else 0
        

        
        if fmaxe == fmaxo:
            save = max(even[fmaxe] + odd[smaxo], odd[fmaxo] + even[smaxe])
        else:
            save = even[fmaxe] + odd[fmaxo]
        
        return len(nums) - save
