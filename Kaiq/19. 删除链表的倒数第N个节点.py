"""
执行用时 : 36 ms, 在Remove Nth Node From End of List的Python提交中击败了12.60% 的用户
内存消耗 : 11.8 MB, 在Remove Nth Node From End of List的Python提交中击败了0.91% 的用户
Method：双指针法.   
"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1=p2=head
        
        for i in range(n):
            p1=p1.next
        if(p1==None):
            return head.next
        while(p1.next!=None):
            p2=p2.next
            p1=p1.next
        print p2.val
        p2.next=p2.next.next
        return head
