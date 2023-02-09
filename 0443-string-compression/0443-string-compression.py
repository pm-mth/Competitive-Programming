class Solution:
    def compress(self, chars: List[str]) -> int:
        
        write = 0
        read = 0
        count = 0
        
        while read < len(chars):
            if count == 0:
                chars[write] = chars[read]
                read += 1
                count += 1
                
            elif count >  1 and chars[write] != chars[read]:
                s = str(count)
        
                for i in range(len(s)):
                    write += 1
                    chars[write] = s[i]     
                count = 0
                write += 1
                
            elif count == 1 and chars[write] != chars[read]:
                write += 1
                count = 0
                
            else:
                count += 1
                read += 1
    
        if count > 1 :
            s = str(count)

            for i in range(len(s)):
                write += 1
                chars[write] = s[i]    
            count = 0
            write += 1
        elif count == 1:
            write += 1
            count = 0
        
        return write