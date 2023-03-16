class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phoneNumber = defaultdict(str)
        phoneNumber["2"] = "abc"
        phoneNumber["3"] = "def"
        phoneNumber["4"] = "ghi"
        phoneNumber["5"] = "jkl"
        phoneNumber["6"] = "mno"
        phoneNumber["7"] = "pqrs"
        phoneNumber["8"] = "tuv"
        phoneNumber["9"] = "wxyz"
        combinations = []
        
        
        def findComb(idx, inter):
            if idx == len(digits):
                combinations.append(deepcopy("".join(inter)))
                return
            
            
            
            for ch in phoneNumber[digits[idx]]:
                inter.append(ch)
                findComb(idx + 1, inter)
                inter.pop()
                
        findComb(0, [])
        return combinations
                
        