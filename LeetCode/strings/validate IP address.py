class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if not queryIP:
            return "Neither"

        def validate(queryIP):
            temp = ""
            i4, i6 = False, False
            alpha = ("a", "b","c","d","e","f", "A", "B", "C", "D", "E", "F")
            count = 0
            for i in range(len(queryIP)):
                if i4 and i6:
                    return "Neither"
                if queryIP[i] == ".":
                    i4 = True
                    count += 1
                    if not temp:
                        return "Neither"
                    if i == len(queryIP) - 1:
                        return "Neither"
                    if len(temp) > 1 and temp[0] == "0":
                        return "Neither"
                    if not temp.isnumeric():
                        return "Neither"
                    if int(temp) > 255:
                        return "Neither"
                    temp = ""
                    continue
                if queryIP[i] == ":":
                    count += 1
                    i6 = True
                    if not temp:
                        return "Neither"
                    if i == len(queryIP) - 1:
                        return "Neither"
                    if len(temp) > 4:
                        return "Neither"
                    for ch in temp:
                        if ch.isalpha():
                            if not ch in alpha:
                                return "Neither"
                    temp = ""
                    continue
                
                temp += queryIP[i]
            
            if i4 and i6:
                return "Neither"
            if i4 and  len(temp) > 1 and temp[0] == "0":
                return "Neither"
            if i4 and not temp.isnumeric():
                return "Neither"
            if i4 and int(temp) > 255:
                return "Neither"
            if i4:
                count += 1
                if count !=  4:
                    return  "Neither"
                return "IPv4"


            if i6 and  len(temp) > 4:
                return "Neither"
            if i6:
                for ch in temp:
                    if ch.isalpha():
                        if not ch in alpha:
                            return "Neither"
            if i6:
                count += 1
                if count !=  8:
                    return  "Neither"
                return "IPv6"
        return validate(queryIP)
                
                                 



        
