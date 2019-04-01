"""
执行用时 : 272 ms, 在Merge k Sorted Lists的Python提交中击败了23.39% 的用户
内存消耗 : 23.5 MB, 在Merge k Sorted Lists的Python提交中击败了3.09% 的用户
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def mergeTwoLists(l1, l2):
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
    
def mergeKLists1(lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if(len(lists)==0):
            return
        if(len(lists)==1):
            return lists[0]
        if(len(lists)==2):
            return mergeTwoLists(lists[0],lists[1])
        mid = len(lists)/2
        l1 = []
        for i in range(0,mid):
            l1.append(lists[i])
        l2=[]
        for i in range(mid,len(lists)):
            l2.append(lists[i])
        return mergeTwoLists(mergeKLists1(l1),mergeKLists1(l2))
    
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return mergeKLists1(lists)
