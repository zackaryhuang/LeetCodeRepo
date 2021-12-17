class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        bottles_drinked = numBottles
        bottles_left = numBottles
        while bottles_left >= numExchange:
            bottles_exchanged = int(bottles_left / numExchange)
            bottles_drinked += bottles_exchanged
            bottles_left = (bottles_left % numExchange) + bottles_exchanged
        return bottles_drinked


if __name__ == '__main__':
    s = Solution()
    print(s.numWaterBottles(15, 4))
