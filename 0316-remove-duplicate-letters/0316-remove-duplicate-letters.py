class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = defaultdict(int)
        
        for i in range(len(s)):
            last_index[s[i]] = i
       
        stack = []
        not_duplicate = set()
        
        for i in range(len(s)):
            while stack and stack[-1] > s[i] and last_index[stack[-1]] > i:
                if s[i] in not_duplicate:
                    break
                    
                if stack[-1] in not_duplicate:
                    not_duplicate.remove(stack[-1])
                    stack.pop() 
                
            if s[i] not in not_duplicate:
                not_duplicate.add(s[i])
                stack.append(s[i])
        
        return "".join(stack)
        