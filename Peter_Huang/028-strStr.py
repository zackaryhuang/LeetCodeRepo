class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                for j in range(0, len(needle)):
                    if (i + j) > len(haystack)-1:
                        return -1
                    if needle[j] == haystack[i + j]:
                        if j == len(needle) - 1 :
                            return i
                        else:
                            continue
                    else:
                        break
                    
        return -1;

if __name__ == "__main__":
    s = Solution()
    print(s.strStr("aaa","aaaa"))
