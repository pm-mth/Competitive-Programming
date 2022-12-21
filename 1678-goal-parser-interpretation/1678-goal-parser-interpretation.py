class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] == "G":
                ans += "G"
            elif command[i] == "(":
                i += 1
                if command[i] == ")":
                    ans += "o"
                else:
                    ans += "al"
                    i += 2
        return ans
        