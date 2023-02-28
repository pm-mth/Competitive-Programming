class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_number = 0
        window = Counter()
        max_fruit = 0
        l = 0
        
        for r in range(len(fruits)):
            window[fruits[r]] += 1
            fruit_number += 1
            
            while  l <= r and len(window) > 2:
                window[fruits[l]] -= 1
                fruit_number -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                max_fruit = max(max_fruit, fruit_number)
                    
                l += 1
                
            
        max_fruit = max(max_fruit, fruit_number)
        
        return max_fruit
                  
        