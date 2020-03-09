import itertools
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        keys = []
        res = []
        for str in strs:
            a = []
            for c in str:
                a.append(ord(c))
            a.sort()
            temp_str = ''
            for i in a:
                temp_str += chr(i)
            
            if temp_str in keys:
                index = keys.index(temp_str)
                res[index].append(str)
            else:
                keys.append(temp_str)
                res.append([str])
        return res
                
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["",""]))