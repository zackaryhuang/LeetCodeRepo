class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A < 2 and B < 2:
            return A * 'a' + B * 'b'
        leftA = A
        leftB = B
        count = 1
        str = ''
        if max(leftA, leftB) == leftB:
            str += 'b'
            leftB -= 1
        else:
            str += 'a'
            leftA -= 1
        while leftA > 0 and leftB > 0:
            if len(str) >= 2:
                if str[-1] == str[-2]:
                    if str[-1] == 'a':
                        str += 'b'
                        leftB -= 1
                    else:
                        str += 'a'
                        leftA -= 1
                else:
                    if max(leftA, leftB) == leftA:
                        str += 'a'
                        leftA -= 1
                    else:
                        str += 'b'
                        leftB -= 1

            else:
                if max(leftA, leftB) == leftA:
                    str += 'a'
                    leftA -= 1
                else:
                    str += 'b'
                    leftB -= 1
            
        if leftB > 0:
            for i in range(leftB):
                str += 'b'
        elif leftA > 0:
            for i in range(leftA):
                str += 'a'
        else:
            return str
        return str

if __name__ == "__main__":
    s = Solution()
    res = s.strWithout3a3b(4,4)
    print(res)




            