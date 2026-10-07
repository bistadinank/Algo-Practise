class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.visited=set()
        self.result = []
        number_of_extra_brackets=self.getMinBrackets(s)
        self.getSolution(s, number_of_extra_brackets)
        return self.result

    def getSolution(self, s, mra):
        if s in self.visited:
            return
        self.visited.add(s)
        
        if mra==0:
            if self.getMinBrackets(s)==0:
                self.result.append(s)
            return
        
        for i in range(len(s)):
            left=s[:i]
            right= s[i+1:]
            self.getSolution(left + right, mra - 1)

    def getMinBrackets(self, s):
        stack=[]
        for i in s:
            if i == "(":
                stack.append(i)
            
            elif i == ")":
                if not stack or stack[-1] == ")":
                    stack.append(i)
            
                else:
                    stack.pop()
        
        return len(stack)