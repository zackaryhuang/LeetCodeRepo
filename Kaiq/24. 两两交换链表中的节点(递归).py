"""
执行用时 : 36 ms, 在Swap Nodes in Pairs的Python提交中击败了4.64% 的用户
内存消耗 : 12 MB, 在Swap Nodes in Pairs的Python提交中击败了0.00% 的用户
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swap(h):
            if not (h and h.next):
                return h
            p=h.next
            q=h.next.next
            h.next=q
            p.next=h
            h.next=swap(h.next)
            return p
        head=swap(head)
        return head
             
