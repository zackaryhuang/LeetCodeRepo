class Solution:
    def generateParenthesis(self, n):
        res = [];
        str = ''
        for i in range(0,n):
            str += '('
        for i in range(0,n):
            str += ')'
        print(str)
        res.append(str)
        for i in range(n - 1,0,-1):
            for j in range(n,2 * n - 1):
                temp_str = list(str)
                a = temp_str[i]
                temp_str[i] = temp_str[j]
                temp_str[j] = a
                b = ''.join(temp_str)
                res.append(b)
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.generateParenthesis(3);
    print(res)
