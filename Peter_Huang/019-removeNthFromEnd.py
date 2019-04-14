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
        ln = head
        l = []
        flag = 0
        while ln != None:
            l.append(ln)
            ln = ln.next
            flag += 1
        if n == 1:
            if flag == 1:
                return None
            else:
                l[flag-n-1].next = None
        elif n == flag:
            head = l[1]
        else:
            l[flag-n-1].next = l[flag-n+1]
        return head