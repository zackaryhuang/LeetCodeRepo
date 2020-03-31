import copy
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        cache = dict()
        for num in deck:
            if str(num) in cache.keys():
                cache[str(num)] += 1
            else:
                cache[str(num)] = 1
        counts = list(cache.values())
        if len(counts) == 1:
            return counts[0] > 1
        # 找counts中最小的两个值的最大公因数
        counts_copy = []
        for num in counts:
            counts_copy.append(num)
        min_1 = min(counts_copy)
        counts_copy.remove(min_1)
        min_2 = min(counts_copy)
        print(min_1,min_2,counts)
        while min_2:
            min_1, min_2 = min_2, min_1 % min_2
        if min_1 % 2 == 0:
            min_1 = 2
        if min_1 > 1:
            for i in counts:
                if i % min_1 == 0:
                    continue
                else:
                    return False
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.hasGroupsSizeX([1,1,1,2,2,2,3,3,3,3,3,3]))