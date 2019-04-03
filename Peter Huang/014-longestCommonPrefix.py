class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = ""
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in range(0,len(strs[0])):
            for j in range(1,len(strs)):
                if strs[j].startswith(strs[0][:i+1]):
                    res = strs[0][:i+1]
                    continue
                else:
                    if strs[0][:i] == "":
                        return ""
                    else:
                        return strs[0][:i]
        return res

def main():
    solution = Solution()
    res = solution.longestCommonPrefix([])
    print(res)

if __name__ == '__main__':
    main()

