class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes_5, notes_10 = 0,0
        for bill in bills:
            diff = bill - 5
            if diff == 15:
                if notes_10:
                    notes_10 -= 1
                    if notes_5:
                        notes_5 -= 1
                    else:
                        return False
                elif notes_5 >= 3:
                    notes_5 -= 3
                else:
                    return False
            elif diff == 5:
                notes_10 += 1
                if notes_5:
                    notes_5 -= 1
                else:
                    return False
            else:
                notes_5 += 1
        return True

                
            

        
