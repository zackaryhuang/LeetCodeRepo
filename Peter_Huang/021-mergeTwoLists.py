# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        while l1 != None and l2 != None:
            l = ListNode(0)
            if l1.val > l2.val:
                l.val = l2.val
                l.next = None
                res.append(l)
                l2 = l2.next
            elif l1.val < l2.val:
                l.val = l1.val
                l.next = None
                res.append(l)
                l1 = l1.next
            elif l1.val == l2.val:
                l.val = l1.val
                l.next = None
                res.append(l)
                l1 = l1.next
            print(l.val,l.next)
        for i in range(len(res)):
            if i != len(res)-1:
                res[i].next = res[i+1]
        if l1 == None and l2 == None:
            return None
        if l1 == None and l2 != None:
            if res == []:
                return l2
            else:
                res[len(res)-1].next = l2
        if l2 == None and l1 != None:
            if res == []:
                return l1
            else:
                res[len(res)-1].next = l1
        return res[0]