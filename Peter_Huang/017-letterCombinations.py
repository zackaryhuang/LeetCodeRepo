from functools import reduce
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return ""
        l = []
        d = []
        for char in digits:
            d.append(char)
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}
        for i in range(len(d)):
            l.append(dict[d[i]])
        fn = lambda x, code='': reduce(lambda x, y: [str(i)+code+str(j) for i in x for j in y], x)
        res = fn(l,'')
        return res
if __name__ == "__main__":
    s = Solution()
    res = s.letterCombinations('')
    print(res)