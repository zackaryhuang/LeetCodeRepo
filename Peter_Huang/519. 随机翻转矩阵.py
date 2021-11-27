import random


class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        random_index = random.randint(0, self.total - 1)
        self.total -= 1
        val = self.map.get(random_index, random_index)
        p_i = val / self.n
        p_j = val % self.n
        self.map[random_index] = self.map.get(self.total, self.total)
        return [p_i, p_j]

    def reset(self):
        """
        :rtype: None
        """
        self.map.clear()
        self.total = self.m * self.n


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
if __name__ == '__main__':
    s = Solution(3, 1)
    s.flip()
