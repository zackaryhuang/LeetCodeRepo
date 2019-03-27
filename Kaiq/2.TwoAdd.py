# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        temp = ans 
        tempsum = 0
        while True:
            if(l1!=None):
                tempsum += l1.val
                l1=l1.next
            if(l2!=None):
                tempsum += l2.val
                l2=l2.next
            temp.val = tempsum%10
            tempsum = int(tempsum/10)
            if l2==None and l1==None and tempsum==0:
                break;
            
            temp.next = ListNode(0)
            temp = temp.next
        return ans
