from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote):
            return False
        counter_note = Counter(ransomNote)
        counter_magz = Counter(magazine)
        for item in counter_note.items():
            key = item[0]
            count = item[1]
            if counter_magz.get(key) < count:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct('aa', 'aba'))