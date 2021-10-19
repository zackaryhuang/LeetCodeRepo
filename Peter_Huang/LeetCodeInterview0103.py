class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        str = S[:length]
        retStr = ""
        for var in str:
            if var == " ":
                retStr += "%20"
            else:
                retStr += var
        return retStr


solution = Solution()
print(solution.replaceSpaces("Mr John Smith    ", 13))