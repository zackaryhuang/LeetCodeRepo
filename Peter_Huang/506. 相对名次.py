import copy


class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_score = sorted(copy.deepcopy(score), reverse=True)
        res = []
        for i in range(len(score)):
            index = sorted_score.index(score[i])
            if index == 0:
                res.append("Gold Medal")
            elif index == 1:
                res.append("Silver Medal")
            elif index == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(index+1))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findRelativeRanks([5,4,3,2,1]))
