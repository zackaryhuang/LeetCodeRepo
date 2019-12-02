class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        step = 1
        s = [0]
        while True:
            new = []
            for num in s:
                if num - step not in s:
                    new.append(num - step)
                if num + step not in s:
                    new.append(num + step)
            s += new
            print(s)
            if target in s:
                return step;
            else:
                step += 1


if __name__ == "__main__":
    s = Solution()
    res = s.reachNumber(-100000)
    print(res)