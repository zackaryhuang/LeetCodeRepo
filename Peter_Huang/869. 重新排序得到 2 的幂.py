from collections import Counter


class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max = 10 ** 9
        candidates = [1]
        cur_pow = 2
        while cur_pow <= max:
            candidates.append(cur_pow)
            cur_pow *= 2
        for candidate in candidates:
            if Counter(str(candidate)).__eq__(Counter(str(n))):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.reorderedPowerOf2(625))