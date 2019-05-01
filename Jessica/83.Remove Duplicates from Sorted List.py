# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:        
        node=head
        while node:
            while node.next and node.val ==node.next.val:
                node.next=node.next.next
            node=node.next
        return head