class Solution(object):
    def halfQuestions(self, questions):
        """
        :type questions: List[int]
        :rtype: int
        """
        dict = {}
        for q_type in questions:
            if q_type in dict.keys():
                dict[q_type] += 1
            else:
                dict[q_type] = 1
        s = sorted(dict.items(), key=lambda item:item[1], reverse=True)
        count = 0
        res = 0
        for value in s:
            count += value[1]
            res += 1
            if count >= len(questions) / 2:
                return res

if __name__ == '__main__':
    s = Solution()
    print(s.halfQuestions([2,1,6,2]))
