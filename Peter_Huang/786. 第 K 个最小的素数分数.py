from functools import cmp_to_key


class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        frac = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                frac.append((arr[i], arr[j]))

        def cmp(x, y):
            return -1 if x[0] * y[1] < y[0] * x[1] else 1

        frac.sort(key=cmp_to_key(cmp))
        return list(frac[k - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallestPrimeFraction([1, 2, 3, 5], 3))
