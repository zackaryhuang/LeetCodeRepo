"""
执行用时 : 72 ms, 在Integer to Roman的Python提交中击败了100.00% 的用户
内存消耗 : 11.7 MB, 在Integer to Roman的Python提交中击败了0.00% 的用户
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a=''
  
        a += 'M' * int(num//1000)
        num=num%1000
        
        a += 'CM'* int(num//900)
        num=num%900
        
        a += 'D' * int(num//500)
        num=num%500
        
        a += 'CD' * int(num//400)
        num=num%400
        
        a += 'C' * int(num//100)
        num=num%100
        
        a += 'XC' * int(num//90)
        num=num%90
        
        a += 'L' * int(num//50)
        num=num%50
        
        a += 'XL' * int(num//40)
        num=num%40
        
        a += 'X' * int(num//10)
        num=num%10
        
        a += 'IX' * int(num//9)
        num=num%9
        
        a += 'V' * int(num//5)
        num=num%5
        
        a += 'IV' * int(num//4)
        num=num%4
      
        a += 'I' * num  
        return a
        
      
