class Solution:
    def intToRoman(self, num):
        res = ''
        if num > 3999 or num < 1:
            return 'N/A'
        thousand = num // 1000
        hundread = (num - thousand * 1000) // 100
        ten = (num - thousand * 1000 - hundread * 100) // 10
        one = num - thousand * 1000 - hundread * 100 - ten * 10
        res += ('M'*thousand)
        if hundread == 9:
            res += 'CM'
        elif hundread > 5:
            res += ('D'+'C'*(hundread-5))
        elif hundread == 5:
            res += ('D')
        elif hundread == 4:
            res += ('CD')
        elif hundread < 4 and hundread > 0:
            res += ('C'*hundread)
        if ten == 9:
            res += 'XC'
        elif ten > 5:
            res += ('L'+'X'*(ten-5))
        elif ten == 5:
            res += ('L')
        elif ten == 4:
            res += ('XL')
        elif ten < 4 and ten > 0:
            res += ('X'*ten)
        if one == 9:
            res += 'IX'
        elif one > 5:
            res += ('V'+'I'*(one-5))
        elif one == 5:
            res += 'V'
        elif one == 4:
            res += 'IV'
        elif one < 4:
            res += ('I'*one)
        return res

def main():
    solution = Solution()
    print(solution.intToRoman(321))
if __name__ == '__main__':
    main()
