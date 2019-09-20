# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str1=''
        str2=''
        while l1:
            str1+=str(l1.val)
            l1=l1.next
        while l2:
            str2+=str(l2.val)
            l2=l2.next
        num1=int(str1[::-1])
        num2=int(str2[::-1])
        num=str(num1+num2)[::-1]
        l3=ListNode(int(num[0]))
        l4=l3
        for i in range(1,len(num)):
            l3.next=ListNode(int(num[i]))
            l3=l3.next
        return l4
            
            
            
        
        
