class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dict = {'0' : 0,
                '1' : 1,
                '2' : 2,
                '3' : 3,
                '4' : 4,
                '5' : 5,
                '6' : 6,
                '7' : 7,
                '8' : 8,
                '9' : 9}
        n1 = 0
        for i in range(0,len(num1)):
            n1 += dict[num1[i]] * 10 ** (len(num1) - i - 1)
        n2 = 0
        for i in range(0, len(num2)):
            n2 += dict[num2[i]] * 10 ** (len(num2) - i - 1)
        
        return str(n1 * n2)

if __name__ == "__main__":
    s = Solution()
    print(s.multiply('0','11'))