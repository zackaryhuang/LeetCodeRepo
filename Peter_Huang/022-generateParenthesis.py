import itertools
class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return ['']
        elif n == 1:
            return ['()']
        resStr = ''
        resList = []
        d = []
        for i in range(0, n):
            d.append(i)
        # for i in range(0, n):
        d = itertools.product(d, repeat=n)
        print('d:', d)
        for item in d:
            print(item)
            for i in item:
                resStr = self.insertParenthesis(i, resStr)
            if resStr in resList:
                resStr = ''
                continue
            else:
                resList.append(resStr)
                resStr = ''
        return resList   

    def insertParenthesis(self, index, parenthesisStr):
        if index == 0:
            return parenthesisStr + '()'
        elif index == 1:
            return '(' + parenthesisStr + ')'
        else:
            return '()' + parenthesisStr
if __name__ == "__main__":
    s = Solution()
    res = s.generateParenthesis(4)
    for item in ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]:
        if item not in res:
            print(item)
    print(res)
