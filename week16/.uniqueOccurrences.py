class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        
        for num in arr:
            count[num] += 1
        checkList = list(count.values())
        checkList.sort()
        for i in range(1, len(checkList)):
            if checkList[i-1] == checkList[i]:
                return False
        return True
        
