class Solution(object):
    def divide(self, dividend, divisor):
        res = 0
        if divisor == 1:
            res = dividend
        elif divisor == -1:
            res = -dividend
        elif abs(dividend) < abs(divisor):
            res = 0
        elif dividend == divisor:
            res = 1
        
        strNum = str(dividend)
        array = []
        for char in strNum:
            array.append(int(char))
        print(array)
        resArray = []
        for num in array:
            a = self.divideByPlace(num, divisor)
            print(a)
            resArray.append(a[0])
            array.pop(0)
            for i in range(0, a[1]):
                array[0] += 10
        print (resArray)

        if res >= -(2 ** 31) and res <= (2 ** 31) - 1:
            return res
        else:
            return 2 ** 31 -1
    def divideByPlace(self, place, divisor):
        # 被除数大于零，除数小于0，商为负
        if place > 0 and divisor < 0:
            count = 2
            sum = divisor
            while(sum <= place):
                sum -= divisor
                print('place:',sum)
                count -= 1
            return [count, place - sum]
        elif place < 0 and divisor > 0:
            count = 2
            sum = divisor
            while(sum >= place):
                sum -= divisor
                count -= 1
            return [count, place - sum]
        elif place >= 0 and divisor > 0:
            count = 0
            sum = 0
            while(sum < place):
                sum += divisor
                count += 1
            return [count, place - sum]
        elif place < 0 and divisor < 0:
            count = 0
            sum = divisor
            while(sum >= place):
                sum += divisor
                count += 1
            return [count, place - sum]

        
if __name__ == '__main__':
    s = Solution()
    res = s.divide(2147483648,2)
    print(res)