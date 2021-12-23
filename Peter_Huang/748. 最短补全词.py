from collections import Counter


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = licensePlate.lower()
        plate_counter = Counter(licensePlate)
        res = ''
        for word in words:
            word_counter = Counter(word)
            bingo = False
            for key in plate_counter.keys():
                if ord(key) < 65:
                    continue
                plate_value = plate_counter.get(key)
                word_value = word_counter.get(key)
                if (word_value is not None) and (word_value >= plate_value):
                    bingo = True
                    continue
                else:
                    bingo = False
                    break
            if bingo and (len(word) < len(res) or res == ''):
                res = word
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.shortestCompletingWord(licensePlate = "OgEu755", words = ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]))