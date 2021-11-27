from collections import Counter
class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        same = []
        diff = []
        for i in range(len(s)):
            if s[i] == goal[i]:
                same.append(s[i])
            else:
                diff.append((s[i], goal[i]))
        if len(diff) != 2 and len(diff) != 0:
            return False
        if len(diff) == 2:
            return diff[0][1] == diff[1][0] and diff[0][0] == diff[1][1]
        else:
            for count in Counter(same).values():
                if count > 1:
                    return True
            return False 

s = Solution()
print(s.buddyStrings("abab", "acaa"))