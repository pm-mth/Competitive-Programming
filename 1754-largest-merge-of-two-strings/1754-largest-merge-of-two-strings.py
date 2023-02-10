class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        result = []
        one = 0
        two = 0 
        while one < len(word1) and two < len(word2):
            if word1[one] > word2[two]:
                result.append(word1[one]) 
                one += 1
            elif word2[two] > word1[one]:
                result.append(word2[two])
                two += 1
            else:
                if word1[one:] >= word2[two:]:
                    result.append(word1[one])
                    one += 1
                else:
                    result.append(word2[two])
                    two += 1
        result.extend(word1[one:])
        result.extend(word2[two:])
        
        return "".join(result)
        