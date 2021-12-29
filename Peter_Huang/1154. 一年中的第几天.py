class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = (int(compStr) for compStr in date.split('-'))
        daysOfFeb = 28
        if year % 4 == 0:
            daysOfFeb = 29
        daysOfMonth = [31, daysOfFeb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return day + sum(daysOfMonth[:month - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.dayOfYear("2004-03-01"))