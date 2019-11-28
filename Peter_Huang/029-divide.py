class Solution(object):
    def divide(self, dividend, divisor):
        res = []
        yushu = abs(dividend)
        while yushu >= abs(divisor):
            shang, yushu, res = self.calculate2(yushu, abs(divisor), res)
            print('shang',shang,'yushu',yushu)
            res.append(shang)
        strNum = ''
        for i in res:
            strNum += str(i)
        temp = []
        for char in strNum:
            temp.append(int(char))
        a = 1
        if dividend > 0 and divisor < 0:
            a = -1
        elif dividend < 0 and divisor > 0:
            a = -1
        else:
            a = 1
        b = a * self.dePreProcessData(temp)
        if b >= (-2) ** 31 and b <= 2 ** 31 -1:
            return b
        else:
            return 2 ** 31 - 1
        

    # 传进来一个除数和被除数，返回商跟剩下的数，如传进来223，3 返回7 和13
    def calculate2(self, dividen, divisor, res):
        array = self.preProcessData(dividen)
        for i in range(len(array)):
            num = 0
            length = len(array[:i+1])
            for j in range(len(array[:i + 1])):
                num += array[j] * 10 ** (length - 1)
                length -= 1
            if num >= divisor:
                shang, yushu = self.calculate(num,divisor)
                a = self.preProcessData(yushu)
                b = []
                if a == [0]:
                    b = array[i + 1:]
                else:
                    b = a + array[i + 1:]
                zeroTimes = 0
                for i in b:
                    if i == 0:
                        zeroTimes += 1
                    else:
                        break
                return shang * 10 ** zeroTimes, self.dePreProcessData(b), res
            # else:
            #     res.append(0)
        
    # 预处理数据，传进来一个数字（正整数），返回数字的各个位的数字，如输入101，返回[1,0,1]
    def preProcessData(self, num):
        strNum = str(num)
        res = []
        for char in strNum:
            res.append(int(char))
        return res

    # preProcessData的逆过程
    def dePreProcessData(self, list):
        num = 0
        length = len(list) - 1
        for j in range(len(list)):
            num += list[j] * 10 ** length
            length -= 1
        return num


    # 传进来一个除数（正整数）和被除数(正整数)，返回商跟余数（只有在数字比较小的时候调用这个方法）
    def calculate(self, dividen, divisor):
        times = 1
        while(divisor * times <= dividen):
            times += 1
        shang = times - 1
        left = dividen - shang * divisor
        return shang, left
        
if __name__ == '__main__':
    s = Solution()
    res = s.divide(2147483647,2)
    print(res)