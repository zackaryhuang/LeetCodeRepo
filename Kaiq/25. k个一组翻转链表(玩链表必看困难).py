"""
执行用时 : 56 ms, 在Reverse Nodes in k-Group的Python提交中击败了14.93% 的用户
内存消耗 : 13.7 MB, 在Reverse Nodes in k-Group的Python提交中击败了0.00% 的用户
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if(k==1 and k==0):
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre = dummy
        cur = head
        len = 0
        while(head!=None):
            len+=1
            head=head.next
        for i in range(0,len/k):
            for j in range(0,k-1):
                if(cur.next != None):
                    nex = cur.next
                    cur.next = nex.next
                    nex.next = pre.next
                    pre.next = nex
            pre = cur
            cur = cur.next
        return dummy.next
