"""
执行用时 : 44 ms, 在Merge Two Sorted Lists的Python提交中击败了9.48% 的用户
内存消耗 : 11.9 MB, 在Merge Two Sorted Lists的Python提交中击败了0.57% 的用户
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        b=head
        while(l1!=None and l2!=None):
            a=ListNode(0)
            if(l1.val>l2.val):
                a.val = l2.val
                l2=l2.next
            else:
                a.val = l1.val
                l1=l1.next
            head.next = a
            head = head.next
        if(l1!=None):
            head.next = l1
        if(l2!=None):
            head.next = l2
        return b.next
