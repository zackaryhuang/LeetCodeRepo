class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cache = {}
        for num in arr:
            if str(num) in cache.keys():
                cache[str(num)] += 1
            else:
                cache[str(num)] = 1
        temp = []
        for num in cache.values():
            if num in temp:
                return False
            else:
                temp.append(num)
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.uniqueOccurrences([1,2]))