class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.answer = []
        self.s = s
        self.validIp(0, [])
        return self.answer
        
        
        
    def validIp(self, i, inter):
        if i == len(self.s) and len(inter) == 4:
            self.answer.append(deepcopy(".".join(inter)))
            return 
        if len(inter) == 4:
            return 
        
        ip = ""
        for j in range(i, len(self.s)):
            ip += self.s[j]
            if len(ip) > 1 and ip[0] == "0":
                return
            if int(ip) > 255:
                return
            inter.append(ip)
            self.validIp(j + 1, inter)
            inter.pop()
            