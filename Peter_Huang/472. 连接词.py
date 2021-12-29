class DictTree(object):
    def __init__(self):
        self.root = {}

    def insert(self, word):
        root = self.root
        for w in word:
            if w not in root:
                root[w] = {}
            root = root[w]
        root['#'] = {}

    def query(self, word):
        if len(word) == 0:
            return True
        root = self.root
        for i, w in enumerate(word):
            if w in root:
                root = root[w]
            else:
                return False
            if '#' in root and self.query(word[i+1:]):
                return True
        return False


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        words.sort(key=lambda x: len(x))
        d_t = DictTree()
        for word in words:
            if not word:
                continue
            if d_t.query(word):
                res.append(word)
            else:
                d_t.insert(word)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))