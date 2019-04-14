class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        
        a = {'(':')',
             '{':'}',
             '[':']'}
        left = ['(','[','{']
        right = [')',']','}']
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if stack == []:
                    return False
                elif char == a[stack[-1]]:
                    stack.pop()
                    continue
                else:
                    return False
        if stack == []:
            return True
        else:
            return False
    
if __name__ == "__main__":
    s = Solution()
    res = s.isValid('[')
    print(res)