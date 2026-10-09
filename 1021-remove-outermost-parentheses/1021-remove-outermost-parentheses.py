class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        res = []
        for i in s:
            if i==")":
                stack.pop()
            if stack:
                res.append(i)
            if i=="(":
                stack.append(i)
        
        return "".join(res)

