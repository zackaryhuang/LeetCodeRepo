import copy
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        length_of_word = len(words[0])
        res = []
        for i in range(len(s)):
            for word in words:
                if i+length_of_word < len(s) and word == s[i : i+length_of_word]:
                    temp_words = copy.copy(words)
                    temp_words.remove(word)
                    j = 1
                    while(len(temp_words) > 0):
                        if (i + (j+1) * length_of_word) < len(s) and s[i + j * length_of_word : i + (j+1) * length_of_word - 1] in temp_words:
                            temp_words.remove(s[i + j * length_of_word : i + (j+1) * length_of_word - 1])
                            j += 1
                        else:
                            break
                    if len(temp_words) == 0:
                        res.append(i)
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring("barfoothefoobarman",["foo","bar"]))
