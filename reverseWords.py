class Solution:
    def reverseWords(self, s: str) -> str:
        stack =[]
        words=s.split()
        for i in words:
            stack.append(i)
            result=""
        while stack:
            result+=" "+stack.pop()

        return result.strip()
            
        
       
