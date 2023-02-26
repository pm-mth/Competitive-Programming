class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        size = len(p)
        newString = ""
        anagram = []
        l = 0
        for r in range(len(s)):
            if r - l + 1 > size:
                window = Counter(newString)
                if window == target:
                    anagram.append(l)
                newString = newString[1:]
                l += 1       
            newString += s[r]
        window = Counter(newString)
        if window == target:
            anagram.append(l)
        return anagram