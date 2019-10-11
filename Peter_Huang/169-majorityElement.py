class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if str(num) in dict.keys():
                dict[str(num)] += 1
            else:
                dict[str(num)] = 1
        print(dict)
        count = 0
        res = 0
        for a in dict.keys():
            if dict[a] > count:
                count = dict[a]
                res = a
        return int(res)


if __name__ == '__main__':
    s = Solution()
    res = s.majorityElement([3,2,3])
    print(res)