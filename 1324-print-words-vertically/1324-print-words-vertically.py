class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        
        #create a dictionary to store the strings at a given index
        vertical_strings = defaultdict(str)
        
        #get the longest string in the llist
        max_string = max(words, key = len)
        max_length = len(max_string)
        
        #store the strings at an appriopriate index
        for word in words:
            for i in range(max_length):
                if i >= len(word):
                    vertical_strings[i] += " "
                else:
                    vertical_strings[i] += word[i]
                    
        #strip the trailing spaces
        vertical_words = []       
        for key in vertical_strings.keys():
            vertical_words.append(vertical_strings[key].rstrip())
            
        return vertical_words
       
       
            
        
        
        