class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open=0
        add=0
        for i in s:
            if i=='(':
                open=open+1
            if i==')':
                if open>0:
                    open-=1
                else:
                    add+=1
                    open=0

        return open+add

    #((())))(