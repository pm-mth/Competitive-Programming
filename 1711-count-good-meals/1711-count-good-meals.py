class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        #count a number's occurance in deliciousness
        count = defaultdict(int)
        for food in deliciousness:
            count[food] += 1
      
        #calculate the difference and check it the dictionary
        result = 0
        for key in count.keys():
            for i in range(22):
                difference = pow(2, i) - key
                if key == difference:
                    freq = count[key]
                    result += (freq**2 - freq )//2   
                elif key != difference and difference in count.keys() :
                    result += count[difference] * count[key]
           
            count[key] = 0
            
        
        return result % (10**9 + 7)
                