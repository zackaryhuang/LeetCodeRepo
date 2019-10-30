import itertools
import copy
class Solution:
    def generateParenthesis(self, n):
        l = list(itertools.product(['(', ')'], repeat=n * 2))
        tem = []
        for i in l:
            tem.append(list(i))
        ress = []
        for i in tem:
            temp = copy.copy(i)
            if self.isValid(i) == True:
                str = ''
                for s in temp:
                    str += s
                ress.append(str)
            else:
                continue
        return ress
        # if self.isValid(['(', '(', '(', ')', ')', '(']):
        #     return True
        # else:
        #     return False

    def isValid(self, t):
        if len(t) == 0:
            return True
        if t[0] == ')':
            return False
        else:
            t.pop(0)
            for i in range(len(t)):
                if t[i] == ')':
                    t.pop(i)
                    return self.isValid(t)
                else:
                    continue


if __name__ == "__main__":
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)
