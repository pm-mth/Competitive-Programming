class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = string.ascii_lowercase
        
        #map the digit to lowercase english alphabet
        dictionary = defaultdict(str)
        for i in range(1, 27):
            if i < 10:
                dictionary[str(i)] = alphabet[i-1]
            else:
                dictionary[str(i) + "#"] = alphabet[i-1]
        
        #generate string from the input
        mapped_string = "" 
        i = 0
        while i < len(s):
            #check if the number is greater 9
            if i + 2 < len(s) and (s[i] == "1" or s[i] == "2") and s[i+2] == "#":
                mapped_string += dictionary[s[i:i+3]]
                i += 3    
            else:
                mapped_string += dictionary[s[i]]
                i += 1
                
                
        return mapped_string
            
            
        
        