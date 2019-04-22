class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stack=[]
        flag=0
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif i==')' and len(stack)>0 and stack[-1]=='(':
                stack=stack[:-1]
            elif i==']' and len(stack)>0 and stack[-1]=='[':
                stack=stack[:-1]
            elif i=='}' and len(stack)>0 and stack[-1]=='{':
                stack=stack[:-1]
            else:                
                return False
        
        if len(stack)==0:
            return True
        else:
            return False
