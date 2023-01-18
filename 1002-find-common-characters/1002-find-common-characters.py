class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        characters = []
        
        for letter in ascii_lowercase:
            
            count = float("inf")
            for word in words:
                if word.count(letter) <= count:
                    count = word.count(letter)
                   
            for _ in range(count):
                characters.append(letter)
                
        return characters
                
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#         words_length = len(words)
#         alphabet = defaultdict(int)
#         for word in words:
#             for ch in word:
#                 alphabet[ch] += 1
        
        
#         repeated_char = []
#         for key in alphabet.keys():
#             if alphabet[key]%words_length == 0:
#                 repetition = alphabet[key]//words_length
#                 for r in range(repetition):
#                     repeated_char.append(key)
#             else:
                
#         return repeated_char
                
        
       
                