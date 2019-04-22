# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode(0)
        l4=ListNode(0)
        l4=l3
        while l1!=None and l2!=None:            
            if l1.val<=l2.val:
                l3.next=ListNode(l1.val)
                l1=l1.next
                l3=l3.next
                
            elif l1.val>l2.val:
                l3.next=ListNode(l2.val)   
                l3=l3.next
                l2=l2.next
               
        while l1!=None: 
            l3.next=ListNode(l1.val)
            l1=l1.next
            l3=l3.next
        while l2!=None: 
            l3.next=ListNode(l2.val)
            l2=l2.next
            l3=l3.next  
        return l4.next
              
        
