class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "\"1\""
        a = 1
        for i in range(1,n):
            a = self.say(a)
        return "\"%d\""%a
    
    def say(self, n):
        numStr = str(n)
        array = []
        for char in numStr:
            array.append(int(char))
        res = []
        if len(array) == 1:
            res.append(1)
            res.append(array[0])
        else:
            count = 1
            for i in range(1, len(array)):
                if array[i-1] == array[i]:
                    count += 1
                    if i == len(array) - 1:
                        res.append(count)
                        res.append(array[i])
                else:
                    res.append(count)
                    res.append(array[i-1])
                    if i == len(array) - 1:
                        res.append(1)
                        res.append(array[i])
                    else:
                        count = 1

        num = 0
        print(res)
        for i in range(0, len(res)):
            num += res[i] * (10 ** (len(res) -1 - i))
        return num

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(6))