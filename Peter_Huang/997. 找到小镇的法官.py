class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trusted = []
        for t in trust:
            if t[0] not in trusted:
                trusted.append(t[0])
        can_law = []
        for i in range(1, n+1):
            if i not in trusted:
                can_law.append(i)
        for law in can_law:
            people = []
            for t in trust:
                if t[1] == law and t[0] not in people:
                    people.append(t[0])
            if len(people) == n - 1:
                return law
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))






