class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        spaced_strings= []
        prev_index = 0
        for index in spaces:
            spaced_strings.append(s[prev_index:index] + " ")
            prev_index = index
        
        spaced_strings.append(s[prev_index:])
        return "".join(spaced_strings)