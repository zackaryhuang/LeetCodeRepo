import copy
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 == '' and s2 == '':
            if s3 != '':
                return False
            else:
                return True
        if s1 == '' and s2 != '':
            if s2 != s3:
                return False
            else:
                return True
        if s1 != '' and s2 == '' :
            if s3 != s1:
                return False
            else:
                return True
        array = []
        index = 0
        for i in range(len(s2)):
            if s2[i] in s3[index:]:
                array.append(s3.index(s2[i], index))
                temp = copy.copy(s3)
                s3 = s3[:s3.index(s2[i], index)] + '*' + s3[s3.index(s2[i], index)+1 :]
                index = temp.index(s2[i], index)
            else:
                return False
        a = array[0]
        for i in range(1, len(array)):
            if array[i] > a:
                a = array[i]
                continue
            else:
                return False
        str = ''
        for s in s3:
            if s != '*':
                str += s
        if str == s1:
            return True
        else:
            return False
        

if __name__ == "__main__":
    s = Solution()
    res = s.isInterleave("aabc","abad","*a*c*ba*")  
    print(res)
